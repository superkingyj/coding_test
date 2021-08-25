import collections
from typing import List
import heapq
import queue

class Solution: 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
        # 0 <- 1
        incourse  = [0] * numCourses
        for dst, start in prerequisites:
            graph[start].append(dst)
            incourse[dst] += 1

        queue = collections.deque([index for index, value in enumerate(incourse) if value == 0])
        visit = set()

        # for i in list(graph):
        #     node = heapq.heappop(queue)
        #     for dst in graph[node]:
        #         heapq.heappush(queue, dst)
        while queue:
            index = queue.popleft()
            print(f"index: {index}, queue:{queue}, visit:{visit}, incourse:{incourse}")
            for dst in graph[index]:
                incourse[dst] -= 1
                if incourse[dst] == 0: queue.append(dst)
        #    incourse[index] -= 1
            visit.add(index)

        print(incourse)
        return len(visit) == numCourses

        # if queue : return False 
        # return True

# 1. 진입차수가 0인 정점을 큐에 삽입합니다
# 2. 큐에서 원소를 꺼내 연결된 모든 간선을 제거합니다
# 3. 간선 제거 이후에 진입차수가 0이 된 정점을 큐에 삽입
# 4. 큐가 빌때까지 2~3 과정 반복

# 0. visit Set 만들기
# 1. prerequisites 를 graph 에 넣기
# 2. while queue
# 3.    진입차수가 0인 정점을 찾아서 큐에 넣기 
# 4.    큐에서 꺼내서 방문하기, 방문한 지역의 진입차수를 1 빼기 (or 그래프에서 간선 제거)
# 5. visit Set 모두 방문했으면 True else False
        
sol = Solution()
print(sol.canFinish(2, [[1,0]])==True)
print(sol.canFinish(2,[[1,0],[0,1]])==False)
print(sol.canFinish(4,[[1,0],[2,1],[3,2],[3,1]])==True)