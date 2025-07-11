import uuid

import redis


class Cache:
    def __init__(self):
        _redis = redis.Redis(host='localhost', port=6379, db=0)
        _redis.flushdb()

    def store(self, data):
        key = uuid.uuid4()
        self._redis.set(key, value)
        return key

    # def get(key, fn):
    #     pass

