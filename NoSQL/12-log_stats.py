#!/usr/bin/env python3
"""Log stats module."""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # 1. Total logs
    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    # 2. Methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # 3. Status check
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check))
