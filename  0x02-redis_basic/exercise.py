#!/usr/bin/env python3
"""
This module provides a Cache class for storing basic data types in Redis.
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for interacting with a Redis database.
    It can store strings, bytes, ints, and floats under a unique key.
    """

    def __init__(self) -> None:
        """
        Initialize the Redis client and flush the database to start fresh.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis with a random key.

        Args:
            data: The data to be stored. Can be a string, bytes, int, or float.

        Returns:
            The generated key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
