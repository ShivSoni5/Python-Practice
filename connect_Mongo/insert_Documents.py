#!/usr/bin/env python

from pymongo import MongoClient
# client = MongoClient()

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017')

db = client.pymongo_new

# db = client['pymongo_test']  # Same as above

# Inserting Documents

posts = db.posts
post_data = {
        'title': 'What is Python?',
        'content': 'Python is a Programming language',
        'author': 'None'
        }
result = posts.insert_one(post_data)
print(f'One post: {result.inserted_id}')
