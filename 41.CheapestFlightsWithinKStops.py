from typing import List
import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights :
            graph[u].append((v,w))
        
        queue = [(0, src, -1)]

        while queue :
            price, node, stop = heapq.heappop(queue)
            if stop > k : continue
            if node == dst : return price
            for v, w in graph[node] :
                alt = price + w
                heapq.heappush(queue, (alt, v, stop+1))
        return -1

# sol = Solution()
# print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)==500)
sol = Solution()
print(sol.findCheapestPrice(4,[[0,3,59],[2,0,83],[2,3,32],[0,2,97],[3,1,16],[1,3,16]], 3, 0, 3))