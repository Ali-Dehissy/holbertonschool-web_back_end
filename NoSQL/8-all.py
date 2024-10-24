#!/usr/bin/env python3
"""
Python function that list all doc
"""

def list_all(mongo_collection):
    """list_all function"""

    docs = mongo_collection.find()

    if docs:
        return list(docs)
    else:
        return []
