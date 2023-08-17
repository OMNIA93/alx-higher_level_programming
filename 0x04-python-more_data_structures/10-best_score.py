#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not len(a_dictionary):
        return None
    max = list(a_dictionary.keys())[0]
    for i in a_dictionary.keys():
        if a_dictionary[i] > a_dictionary[max]:
            max = i
    return max
