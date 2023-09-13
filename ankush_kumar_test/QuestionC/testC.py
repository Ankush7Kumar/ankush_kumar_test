import unittest
import time
from geoDistributedLRUCache import GeoDistributedLRUCache

# We test GeoDistributedLRUCache with TestGeoDistributedLRUCache.

class TestGeoDistributedLRUCache(unittest.TestCase):
    def setUp(self):
        # Initialize a GeoDistributedLRUCache for testing
        self.cache = GeoDistributedLRUCache(capacity=2, default_ttl=3600)

    def test_put_get(self):
        # Test adding and retrieving items from the cache
        self.cache.put("2", "valueforkey2", ttl=10)
        self.assertEqual(self.cache.get("2"), "valueforkey2")

    def test_default_ttl(self):
        # Test using the default TTL for an item
        self.cache.put("4", "valueforkey4")
        self.assertEqual(self.cache.get("4"), "valueforkey4")

    def test_ttl_expiry(self):
        # Test TTL expiration for an item
        self.cache.put("6", "valueforkey6", ttl=1)  # TTL set to 1 second
        time.sleep(2)  # Wait for the item to expire
        self.assertIsNone(self.cache.get("6"))  # Item should be expired

    def test_capacity_eviction(self):
        # Test LRU eviction when cache exceeds capacity
        self.cache.put("2", "valueforkey2")
        self.cache.put("4", "valueforkey4")
        self.cache.put("6", "valueforkey6")  # Adding one more item should trigger eviction
        self.assertIsNone(self.cache.get("2"))  # 2 should be evicted

    def test_remove(self):
        # Test removing an item from the cache
        self.cache.put("2", "valueforkey2")
        self.cache.remove("2")
        self.assertIsNone(self.cache.get("2"))  # 2 should be removed



if __name__ == '__main__':
    unittest.main()
