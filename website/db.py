# coding: utf-8

import settings
from pymongo import Connection
from pymongo.objectid import ObjectId

_connection = Connection(settings.MONGODB_HOST, settings.MONGODB_PORT)
_db = _connection[settings.MONGODB_NAME]

def get_db():
    return _db
