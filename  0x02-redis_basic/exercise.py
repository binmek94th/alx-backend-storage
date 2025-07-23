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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
            """
            Retrieve data from Redis by key. Optionally apply a conversion function.

            Args:
                key: The Redis key to retrieve.
                fn: Optional callable to convert the returned bytes to the expected type.

            Returns:
                The retrieved data, optionally converted by fn, or None if key doesn't exist.
            """
            value = self._redis.get(key)
            if value is None:
                return None
            if fn:
                return fn(value)
            return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string value from Redis.

        Args:
            key: The Redis key to retrieve.

        Returns:
            The string value, or None if key doesn't exist.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value from Redis.

        Args:
            key: The Redis key to retrieve.

        Returns:
            The integer value, or None if key doesn't exist.
        """
        return self.get(key, lambda d: int(d))

