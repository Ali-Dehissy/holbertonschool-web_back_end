#!/usr/bin/env python3
"""Python function that inserts new document"""

def insert_school(mongo_collection, **kwargs):
    """Mongo function"""
    document_id = mongo_collection.insert(kwargs)
    return document_id
