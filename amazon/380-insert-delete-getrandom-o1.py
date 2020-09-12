"""
https://leetcode.com/problems/insert-delete-getrandom-o1/

380. Insert Delete GetRandom O(1)

Design a data structure that supports all following operations in average O(1) time.

 
insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.
 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom always return 2.
 

Constraints:

-231 <= val <= 231 - 1
At most 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.


https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/455253/Python-or-Super-Efficient-or-Detailed-Explanation

A set is implemented essentially the same as a dict in python, 
so the time complexity of add / delete is on average O(1). 
When it comes to the random function, however, we run into the problem of 
needing to convert the data into a python list in order to return a random element. 
That conversion will add a significant overhead to getRandom, 
thus slowing the whole thing down.

Instead of having to do that type conversion (set to list) 
we can take an approach that involves maintaining both a list and a dictionary side by side. 


"""

import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_data = {}
        self.data = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict_data:
            return False
        self.dict_data[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict_data:
            return False
        val_index = self.dict_data[val]
        self.dict_data[self.data[-1]] = val_index
        self.data[val_index] = self.data[-1]

        self.dict_data.pop(val)
        self.data.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
