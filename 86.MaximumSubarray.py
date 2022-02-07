from typing import *

class Solution:
    def memorization(self, nums: List[int]) -> int:
        if not nums: return 0
        _sum = [nums[0]]
        for num in nums[1:]:
            currentSum = num + _sum[-1]
            _sum.append(max(currentSum,num))
        print(_sum)
        return max(_sum)

    def kadane(self, nums: List[int]) -> int:
        bestMax = nums[0]
        currentSum = 0
        for num in nums:
            currentSum = max(num, num + currentSum)
            bestMax = max(bestMax, currentSum)
        return bestMax

    def maxSubArray(self, nums: List[int]) -> int:
        return self.kadane(nums)

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(a.maxSubArray([1]))
print(a.maxSubArray([5,4,-1,7,8]))

# 3 * 10^4
# O(n^2) ==> 9 * 10^8 =~ 10^9 1G
# O(n log n)