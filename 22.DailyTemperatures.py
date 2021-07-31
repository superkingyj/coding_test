from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for _index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1] :
                (targetIndex, _) = stack.pop()
                result[targetIndex] = _index - targetIndex
            stack.append((_index, temp))
        return output

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result = []
        # stack = list(reversed(temperatures))
        # for i in range(len(temperatures)) :
        #     stack_ = stack[:-i-1:]
        #     stackLen = len(stack_)
        #     day = 1
        #     temp = temperatures[i]
        #     while stack_ != [] and temp >= stack_.pop() : 
        #         day += 1
        #     if day == stackLen+1 : day = 0
        #     result.append(day)
        # return result