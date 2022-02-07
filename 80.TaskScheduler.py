from typing import *
import collections
import heapq

'''
    collections.Counter([1,1,1,1,3,4,5,4])
Counter({1: 4, 4: 2, 3: 1, 5: 1})
for key, value in dict.items()
'''
class Solution:
    def runCPU(self, heap: List[Tuple[int, int, str]]):
        for item in heap:
            if item[0] > 0: item[0] -= 1
        
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)

        heap = []
        for task, count in counter.items():
            heapq.heappush(heap, [0, -count, task])

        time = 0
        # 1 <= task.length <= 10^4
        # O(n^2 log n)
        # (10^8 * 4) * 8 == 3.3 * 10^9 (== 3300 ms)
        # if O(n^2) --> 800 ms
        # if O(n log n) : 10^4 * 4 --> 40k 0.0x ms (xx us), (0.0000x s)
        while heap: # n
            print(f"heap : {heap}")
            task = heapq.heappop(heap) # log(n)
            if task[0] > 0:
                heapq.heappush(heap, task) # log(n)
                print(f"{task} idle")
            elif task[0] <= 0: 
                print(f"{task} {task[2]}")
                task[1] += 1
                task[0] = n + 1
                if task[1] == 0: pass
                else: heapq.heappush(heap, task) # log(n)
            
            self.runCPU(heap) # 맨 앞의 restTime을 1씩 뺀다 n
            heapq.heapify(heap) # n log n
            time +=1
        return time

# n = 4
# heapq([(3, -3 "A"), (1, -3, "B")])
# 0 idle
# heapq([(2, -3, "A"), (0, -3, "B")])
# 1 B
# heapq([(1, -3, "A"), (3, -2, "B")]) 
# 2 idle
# heapq([(0, -2, "A"), (2, -2, "B")]) 
# 3 A
# heapq([(3, -2, "A"), (1, -2, "B")]) 
# 4 idle

print(Solution().leastInterval(
    tasks = ["A","A","A","B","B","B"], n = 2) == 8)
print(Solution().leastInterval(
   tasks = ["A","A","A","B","B","B"], n = 0) == 6)
print(Solution().leastInterval(
   tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2) == 16)
