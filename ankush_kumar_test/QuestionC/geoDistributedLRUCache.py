# To reduce latency in our Geo Distributed LRU Cache, we will use redis
# We install redis by running this bash command "pip install redis"

import redis
import time

class GeoDistributedLRUCache:
    def __init__(self, capacity, default_ttl):
        self.capacity = capacity
        self.default_ttl = default_ttl
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    def get(self, key):
        value = self.redis_client.get(key)
        if value is None:
            return None

        expiration_time = self.redis_client.get(key + ':ttl') # TTL stands for 'time to live'
        if expiration_time is None or float(expiration_time) < time.time():
            self.remove(key)
            return None

        return value

    def put(self, key, value, ttl=None):
        ttl = ttl if ttl is not None else self.default_ttl
        expiration_time = time.time() + ttl

        # Store the value and expiration time in Redis
        self.redis_client.set(key, value)
        self.redis_client.set(key + ':ttl', expiration_time)

        # Implement LRU eviction if the cache exceeds capacity
        self.lru_eviction()

    def remove(self, key):
        self.redis_client.delete(key)
        self.redis_client.delete(key + ':ttl')

    def lru_eviction(self):
        keys = self.redis_client.keys()
        if len(keys) > self.capacity:
            # Sort keys by their expiration time
            keys.sort(key=lambda k: float(self.redis_client.get(k + ':ttl')))
            # Remove the oldest (LRU) keys until the capacity is met
            for key in keys[:len(keys) - self.capacity]:
                self.remove(key)
