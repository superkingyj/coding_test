from typing import List

class Solution:
    def combine(self, n:int, k:int) -> List[List[int]]:
        results = []

        def dfs(elements, start:int, k:int):
            if k==0:
                results.append(elements[:])
                return
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        
        dfs([], 1, k)
        return results

# def combination(numbers, register, k <-- (len))
# combination([1,2,3], [], 2) --> combination([2,3], [1], 1) + combination([3], [2], 1) + combination([], [3], 1)
# combination([2,3], [1], 1) --> combination([3], [1,2], 0)

# def combination(4, ??) -> [??, 4], [??, 4] -> 4-1
# def combination(3, ??) -> [??, 3], 

sol = Solution()
print(sol.combine(4, 2))
print(sol.combine(1,1))

'''
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''

'''
[[1]]
'''
