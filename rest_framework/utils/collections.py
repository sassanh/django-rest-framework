"""
Helper functions for collections.
"""
import collections


def merge(first_dictionary, second_dictionary):
    """
    Merges 2 Mappings, suitable for results of formencode
    """
    merged = first_dictionary.copy()
    for key, value in second_dictionary.items():
        if isinstance(value, collections.Mapping):
            merged_value = merge(merged.get(key, {}), value)
            merged[key] = merged_value
        elif (
            key in merged and
            isinstance(merged[key], collections.Sized) and
            isinstance(value, collections.Sized) and
            len(merged[key]) == len(second_dictionary[key])
        ):
            merged_value = []
            for (v1, v2) in zip(merged[key], second_dictionary[key]):
                merged_value.append(merge(v1, v2))
            merged[key] = merged_value
        else:
            merged[key] = second_dictionary[key]
    return merged
