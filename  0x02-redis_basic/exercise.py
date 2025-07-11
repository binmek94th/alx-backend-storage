#!/usr/bin/env python3
"""
Redis cache exercise module
"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self) -> None:
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis under a random key.

        Args:
            data (str | bytes | int | float): The data to store.

        Returns:
            str: The randomly generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
