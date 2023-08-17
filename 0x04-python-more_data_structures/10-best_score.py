#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = None
    best_student = None
    for student, score in a_dictionary.items():
        if max_score is None or score > max_score:
            max_score = score
            best_student = student
    return best_student
