#!/usr/bin/env python3
"""Changes all topics"""
def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school documnet"""
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
