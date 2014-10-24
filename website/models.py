# -*- coding:utf-8 -*-
from pymongo.objectid import ObjectId

import db


class Entry(object):
    _db = db.get_db()['texts']

    def __init__(self, title, text, cover=''):
        self.title = title
        self.text = text
        self.cover = cover

    @classmethod
    def create(cls, title, text, cover=''):
        obj = Entry(title, text, cover)
        doc = {'title': title, 'text': text}
        if cover:
            doc['cover'] = cover
        obj.id = cls._db.insert(doc)
        return obj

    @classmethod
    def delete(cls, _id):
        return cls._db.remove({'_id': ObjectId(_id)})

    @classmethod
    def get(cls, _id):
        doc = cls._db.find_one({'_id': ObjectId(_id)})
        obj = None
        if doc:
            _id = doc.pop('_id')
            obj = Entry(**doc)
            obj.id = _id
        return obj

    @classmethod
    def get_list(cls, limit=10, page=0):
        skip = limit * page
        docs = cls._db.find({}, limit=limit, skip=skip)
        objs = []
        for doc in docs:
            _id = doc.pop('_id')
            obj = Entry(**doc)
            obj.id = _id
            objs.append(obj)
        return objs
