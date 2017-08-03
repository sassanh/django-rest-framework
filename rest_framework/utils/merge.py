"""
Helper function for merging mappings
"""
import collections

def update(dictionary1, dictionary2):
    merged = dictionary1.copy()
    for key, value in dictionary2.items():
        if isinstance(value, collections.Mapping):
            updated_value = update(merged.get(key, {}), value)
            merged[key] = updated_value
        else:
            merged[key] = dictionary2[key]
    return merged
