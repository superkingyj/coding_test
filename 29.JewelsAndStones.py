import collections
from typing import *

class Solution:
    # O(jewels.len + stones.len)
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # return sum([1 for s in stones if s in jewels])
        # O(jewels.len * stones.len)

        jewel_dict = collections.defaultdict(int)
        for item in jewels :
            jewel_dict[item] = 0
        for stone in stones :
            if stone in jewel_dict:
                jewel_dict[stone] += 1
        return sum(jewel_dict.values())

# jewels --> split --> jewel_dict
# counter = 0
# for stone in stones: if found jewel from stone --> counter++
# return counter
sol = Solution()
print(sol.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(sol.numJewelsInStones(jewels = "z", stones = "ZZ"))
