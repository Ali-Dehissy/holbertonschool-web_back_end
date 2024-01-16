#!/usr/bin/env python3
"""Python function that lists all documents"""
def list_all(mongo_collection):
    """Returns an empty list if none found"""
    doc = mongo_collection.find()
    if doc.count() == 0:
        return []
    else:
        return doc
