#!/usr/bin/env python

from pymongo import MongoClient
client = MongoClient()

db = client.pymongo_new

posts = db.posts
william_post = posts.find_one({'author': 'William'})
print(william_post)
