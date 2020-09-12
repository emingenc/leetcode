"""
https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/submissions/

381. Insert Delete GetRandom O(1) - Duplicates allowed

Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. 
The probability of each element being returned is linearly related to the number 
of same value the collection contains.


Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();

"""

import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_data = {}  # key: val. value: set of index
        self.data = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.data.append(val)
        if val not in self.dict_data:
            self.dict_data[val] = set([len(self.data) - 1])
            return True
        self.dict_data[val].add(len(self.data) - 1)
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.data or val not in self.dict_data.keys():
            return False

        last_val = self.data[-1]
        last_index = len(self.data) - 1
        val_i = self.dict_data[val].pop()
        self.data[val_i] = last_val
        self.data.pop()

        self.dict_data[last_val].add(val_i)
        self.dict_data[last_val].remove(last_index)
        if not self.dict_data[val]:
            del self.dict_data[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.data)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
