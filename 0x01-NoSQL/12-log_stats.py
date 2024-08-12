#!/usr/bin/env python3
"""
This script connects to a MongoDB database and retrieves statistics about Nginx logs.
The stats include the total number of logs, the count of logs by method type, 
and the number of logs with specific path and method.
"""

from pymongo import MongoClient

# Connect to the MongoDB server running on localhost with the default port 27017
client = MongoClient('mongodb://127.0.0.1:27017')

# Access the 'logs' database
db = client.logs

# Access the 'nginx' collection within the 'logs' database
collection = db.nginx

# Get the total number of documents (logs) in the collection
total_logs = collection.count_documents({})
print(f"{total_logs} logs")

# Print a header for the methods section
print("Methods:")

# List of HTTP methods to check
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

# Loop through each method and count how many documents have that method
for method in methods:
    # Count the documents where the 'method' field matches the current method
    method_count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {method_count}")

# Count the number of documents where the 'method' is 'GET' and the 'path' is '/status'
status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_check_count} status check")
