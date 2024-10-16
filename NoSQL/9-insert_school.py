#!/usr/bin/env python3
"""Insert a document"""


def insert_school(mongo_collection, **kwargs):
    """ Function that inserts a new document
    in a collection based on kwargs"""
    result = mongo_collection.insert_one(kwargs)
    return result and result.inserted_id
