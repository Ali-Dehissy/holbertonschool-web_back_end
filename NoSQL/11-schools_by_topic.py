#!/usr/bin/env python3
""" 
Python function that returns the list of
school having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """Mongo function"""
    documents = mongo_collection.find({"topics": topic})
    list_docs = [i for i in documents]
    return list_docs
