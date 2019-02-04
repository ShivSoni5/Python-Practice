#!/usr/bin/env python

from pymongo import MongoClient
client = MongoClient()

db = client.pymongo_new

posts = db.posts
post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Styris'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'William'
}
post_4 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'William'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}

result = posts.insert_many([post_1,post_2,post_3,post_4])
print(f'Mulitple Posts: {result.inserted_ids}')
