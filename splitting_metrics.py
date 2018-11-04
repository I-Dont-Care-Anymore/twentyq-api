from typing import Set, Dict, Callable


TagSimilarity = Dict[str, float]
CategoryFreqs = Dict[int, TagSimilarity]
Attributes = Set[str]
MetricCallable = Callable[[
    Attributes, CategoryFreqs, float, CategoryFreqs, CategoryFreqs], str]


def even(attributes: Attributes, categories_tags_dict: CategoryFreqs, threshold: float, left: CategoryFreqs, right: CategoryFreqs) -> str:
    # compute the best metric
    tag_frequencies: Dict[str, int] = {}  # map frequencies of tags
    distance: float = 0.5 * len(categories_tags_dict)

    tag_value_map: TagSimilarity
    for tag_value_map in categories_tags_dict.values():  # list of all attributes and values
        for tag in attributes:  # iterate over all viable splitting attributes
            if tag_value_map[tag] > threshold:
                if tag in tag_frequencies:
                    tag_frequencies[tag] += 1
                else:
                    tag_frequencies[tag] = 1

    best_tag: str = max(tag_frequencies.items(),
                        key=lambda tup: abs(tup[1] - distance))[0]

    category: int
    tag_value_map: TagSimilarity
    for category, tag_value_map in categories_tags_dict.items():
        if tag_value_map[best_tag] < threshold:
            left[category] = tag_value_map
        else:
            right[category] = tag_value_map

    return best_tag
