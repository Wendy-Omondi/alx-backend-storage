#!/usr/bin/env python3
"""function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    return list(mongo_collection.find())
