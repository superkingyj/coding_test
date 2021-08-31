from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        benefit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]: benefit += prices[i+1] - prices[i]
        return benefit
        

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4])==7)
print(sol.maxProfit([1,2,3,4,5])==4)
print(sol.maxProfit([7,6,4,3,1])==0)