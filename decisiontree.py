
# list of attribute [home, electronic, appliance, etc.] along with potential values in a hash set to linked list
# some of these quesitons will be hyper-specific to category at one point => when we'll enter a different solver
# possibly even more
# a list of NAICs codes => plan to stop at 4-digits for now


#   if node is just single then return me of potential elements
#   metric evaluate best attribute (use this metric to split the categories) create a node with the metric specified and the value
#   connect its pointers to another build-tree(node)
#   at leaf node you must make a decision


# use the highest gini index value
# https://dataaspirant.com/2017/01/30/how-decision-tree-algorithm-works/


# a map of category names to a map of attributes with values (nested dictionary)
from typing import List, Dict
import random
import splitting_metrics

from naics import cross_references
from spacy.tokens import Token


class Node(object):

    def __init__(self, max_depth: int, attributes: splitting_metrics.Attributes, categories_tags_dict: splitting_metrics.CategoryFreqs, value: int, parent):
        self.max_depth = max_depth
        self.attributes = attributes
        self.categories_tags_dict = categories_tags_dict
        self.value = value
        self.parent = parent

    def induct(self, index: int):
        if len(self.categories_tags_dict.keys()) == 0:
            return Node(max_depth=self.max_depth, attributes=self.attributes, categories_tags_dict=self.categories_tags_dict, value=-1, parent=self)
        elif len(categories_tags_dict) == 1:
            # make the category the root
            return Node(max_depth=self.max_depth, attributes=self.attributes, categories_tags_dict=self.categories_tags_dict, value=list(categories_tags_dict.keys())[0], parent=self)
        # choose an arbitrary category because no more decisions can be made
        elif len(self.attributes) == 0 or len(attributes) - len(self.attributes) >= self.max_depth - 1:
            return Node(max_depth=self.max_depth, attributes=self.attributes, categories_tags_dict=self.categories_tags_dict, value=random.choice(list(categories_tags_dict.keys())), parent=self)
        else:
            left: splitting_metrics.CategoryFreqs = {}
            right: splitting_metrics.CategoryFreqs = {}

            new_node_value = splitting_metrics.even(
                self.attributes, categories_tags_dict, 0.5, left, right)

            attributes_copy = self.attributes.copy()
            attributes_copy.remove(new_node_value)

            if index == 0:
                new_categories_tags_dict = left
            elif index == 1:
                new_categories_tags_dict = self.categories_tags_dict
            elif index == 2:
                new_categories_tags_dict = right
            return Node(max_depth=self.max_depth, attributes=attributes_copy, categories_tags_dict=new_categories_tags_dict, value=new_node_value, parent=self)


class TreeClassifier(object):

    def __init__(self, attributes: splitting_metrics.Attributes, categories_tags_dict: splitting_metrics.CategoryFreqs, max_depth: int):
        root_value = splitting_metrics.even(
            attributes, categories_tags_dict, 0.5, {}, {})
        attributes.remove(root_value)
        for tag_value_map in categories_tags_dict.values():
            tag_value_map.pop(root_value)
        self.root = Node(max_depth=max_depth, attributes=attributes.copy(
        ), categories_tags_dict=categories_tags_dict, value=root_value, parent=None)


attributes: Dict[str, Token] = {}

for code, doc in cross_references.items():
    for token in doc:
        if token.tag_ == 'NNPS' or token.tag_ == 'NNP' or token.tag_ == 'NN' or token.tag_ == 'VB':
            attributes[token.norm_] = token

categories_tags_dict: splitting_metrics.CategoryFreqs = {}
print(f'There are {len(attributes)} attributes')

for code, doc in cross_references.items():
    tag_freqs: splitting_metrics.TagSimilarity = {}
    for token_norm, token in attributes.items():
        tag_freqs[token_norm] = token.similarity(doc)
    categories_tags_dict[code] = tag_freqs


questions_tree = TreeClassifier(
    [token_norm for token_norm in attributes.keys()], categories_tags_dict, max_depth=20)
