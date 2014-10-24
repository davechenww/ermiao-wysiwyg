# -*- coding:utf-8 -*-

from pymongo import Connection

import db

db = db.get_db()
texts = db['texts']    #texts is a collection name

def insert(doc):
    return texts.insert(doc)

def delete(text_id):
    return texts.remove({'_id': text_id})

def get_text(text_id):
    doc = texts.find_one({'_id': text_id})
    text = doc['text']
    return text

def get_title(text_id):
    doc = texts.find_one({'_id': text_id})
    title = doc['title']
    return title
