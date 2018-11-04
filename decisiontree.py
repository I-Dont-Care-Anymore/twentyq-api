
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

    def __init__(self, value: int, parent, children: List = []):
        self.value = value
        self.parent = parent
        self.children = children

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret


class TreeClassifier(object):

    def __init__(self, attributes: splitting_metrics.Attributes, categories_tags_dict: splitting_metrics.CategoryFreqs, max_depth: int, split_metric: splitting_metrics.MetricCallable = splitting_metrics.even):
        self.max_depth = max_depth
        self.attributes = attributes
        self.categories_tags = categories_tags_dict
        self.split_metric = split_metric
        self.root = self.induct_tree(
            self.attributes.copy(), self.categories_tags, None)

    def induct_tree(self, attributes: splitting_metrics.Attributes, categories_tags_dict: splitting_metrics.CategoryFreqs, parent: Node) -> Node:
        if len(categories_tags_dict.keys()) == 0:
            return Node(-1, parent)
        elif len(categories_tags_dict) == 1:
            # make the category the root
            return Node(list(categories_tags_dict.keys())[0], parent)
        # choose an arbitrary category because no more decisions can be made
        elif len(attributes) == 0 or len(self.attributes) - len(attributes) >= self.max_depth - 1:
            return Node(random.choice(list(categories_tags_dict.keys())), parent)
        else:
            left: splitting_metrics.CategoryFreqs = {}
            right: splitting_metrics.CategoryFreqs = {}

            new_node_value = self.split_metric(
                attributes, categories_tags_dict, 0.5, left, right)

            attributes_copy = attributes.copy()
            attributes_copy.remove(new_node_value)

            new_node: Node = Node(new_node_value, parent)
            new_node.children = [self.induct_tree(attributes_copy, left, new_node),
                                 self.induct_tree(
                attributes_copy, categories_tags_dict, new_node),
                self.induct_tree(attributes_copy, right, new_node)]
            return new_node

    def print_tree(self):
        print(self.root)


attributes: Dict[str, Token] = {}

for code, doc in cross_references.items():
    for token in doc:
        # if token.pos_ == 'VERB' or token.pos_ == 'NOUN':
        if token.tag_ == 'NNPS' or token.tag_ == 'NNP' or token.tag_ == 'VB' or token.tag_ == 'NN':
            attributes[token.norm_] = token

categories_tags_dict: splitting_metrics.CategoryFreqs = {}
print(f'There are {len(attributes)} attributes')

for code, doc in cross_references.items():
    tag_freqs: splitting_metrics.TagSimilarity = {}
    for token_norm, token in attributes.items():
        tag_freqs[token_norm] = token.similarity(doc)
    categories_tags_dict[code] = tag_freqs

questions_tree = TreeClassifier(
    [token_norm for token_norm in attributes.keys()], categories_tags_dict, max_depth=10)
