# coding: utf-8
from django.conf import settings

from pymongo import Connection

_connection = Connection(settings.MONGODB_HOST, settings.MONGODB_PORT)
_db = _connection[settings.MONGODB_NAME]


def get_db():
    return _db
