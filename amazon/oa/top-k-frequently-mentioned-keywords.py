"""
Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to least frequently mentioned.

The comparison of strings is case-insensitive.
Multiple occurances of a keyword in a review should be considred as a single mention.
If keywords are mentioned an equal number of times in reviews, sort alphabetically.

----------------------
Example 1:

Input:
k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]

Output:
["anacell", "betacellular"]

Explanation:
"anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.


Example 2:

Input:
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

Output:
["betacellular", "anacell"]

Explanation:
"betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews, but "anacell" is lexicographically smaller.
Related problems:

https://leetcode.com/problems/top-k-frequent-words/
https://leetcode.com/problems/top-k-frequent-elements/

"""

import collections
import heapq
from typing import List


class Element:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq


def topKFrequent(keywords: List[str], reviews: List[str], k: int) -> List[str]:
    word_list = []
    for review in reviews:
        word_list += set(review.lower().replace('[^a-z0-9]', '').split())
    count = collections.Counter(word_list)
    heap = []
    for word, freq in count.items():
        if word in keywords:
            heapq.heappush(heap, (-freq, word))
            # heapq.heappush(heap, Element(word, freq))
            # if len(heap) > k:
            #    heapq.heappop(heap)
    # return [heapq.heappop(heap).word for _ in range(k)][::-1]
    return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    for args in (
        (
            ["anacell", "cetracular", "betacellular"],
            [
                "Anacell provides the best services in the city",
                "betacellular has awesome services",
                "Best services provided by anacell, everyone should use anacell",
            ],
            2,
        ),
        (
            ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"],
            [
                "I love anacell Best services; Best services provided by anacell",
                "betacellular has great services",
                "deltacellular provides much better services than betacellular",
                "cetracular is worse than anacell",
                "Betacellular is better than deltacellular.",
            ],
            2,
        ),
    ):
        print(*args)
        print(topKFrequent(*args))
