#!/usr/bin/env python

from pymongo import MongoClient
client = MongoClient()

db = client.pymongo_new

posts = db.posts
# william_post = posts.find_many({'author': 'William'})
william_post = posts.find({'author': 'William'})
for i in william_post:
    print(i)
print()

every_post = posts.find()
for i in every_post:
    print(i)
