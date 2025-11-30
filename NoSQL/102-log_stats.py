#!/usr/bin/env python3
"""Log stats module with Top 10 IPs."""
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

    # 4. Top 10 IPs
    print("IPs:")
    top_ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for ip in top_ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))
