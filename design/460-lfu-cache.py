"""
https://leetcode.com/problems/lfu-cache/

460. LFU Cache

Design and implement a data structure for Least Frequently Used (LFU) cache. 
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, 
otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 
When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls 
to the get and put functions for that item since it was inserted. 
This number is set to zero when the item is removed.


Follow up:
Could you do both operations in O(1) time complexity?


Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""

from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.vals = dict()                               # key, value
        self.counts = dict()                             # key, counts
        self.seq = defaultdict(OrderedDict)  # count, [key, value]
        self.capacity = capacity
        self.minCount = 0

    def get(self, key: int) -> int:
        # 1. find key
        if not key in self.vals:
            return -1

        # 2. add count
        count = self.counts[key]
        self.counts[key] = count + 1

        # 3. remove from sequence and add to a new sequence
        del self.seq[count][key]

        # if count + 1 not in self.seq:
        #    self.seq[count + 1] = OrderedDict()
        self.seq[count + 1][key] = self.vals[key]

        # if the count of the current key count == minCount and
        # if the len of seq[count] == 0
        if count == self.minCount and len(self.seq[count]) == 0:
            self.minCount += 1

        return self.vals[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        # 1. values contains key
        if key in self.vals:
            self.vals[key] = value
            self.get(key)
            return

        # 2. size >= capacity
        if len(self.vals) == self.capacity:
            delKey, _ = self.seq[self.minCount].popitem(last=False)
            del self.vals[delKey]
            del self.counts[delKey]

        # 3. add key
        self.vals[key] = value
        self.counts[key] = 1
        self.seq[1][key] = OrderedDict()
        self.minCount = 1

        return
