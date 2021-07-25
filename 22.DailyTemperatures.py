from typing import List
from copy import deepcopy

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        stack = list(reversed(temperatures))
        for i in range(len(temperatures)) :
            stack_ = stack[:-i-1:]
            stackLen = len(stack_)
            day = 1
            temp = temperatures[i]
            while stack_ != [] and temp >= stack_.pop() : 
                day += 1
            if day == stackLen+1 : day = 0
            result.append(day)
        return result
