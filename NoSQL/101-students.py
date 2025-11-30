#!/usr/bin/env python3
"""Top students module."""


def top_students(mongo_collection):
    """Return all students sorted by average score."""
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": { "$avg": "$topics.score" }
            }
        },
        {
            "$sort": { "averageScore": -1 }
        }
    ])
