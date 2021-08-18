from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost) : return -1

        leftGas, start = 0, 0
        for i in range(len(gas)):
            if gas[i] + leftGas < cost[i]:
                start = i+1
                leftGas = 0
            else :
                leftGas += gas[i] - cost[i]
        return start

sol = Solution()
print(sol.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])==3)
print(sol.canCompleteCircuit([2,3,4],[3,4,3])==-1) 
print(sol.canCompleteCircuit([5,1,2,3,4],[4,4,1,5,1])==4)
print(sol.canCompleteCircuit([5,8,2,8],[6,5,6,6])==3)
