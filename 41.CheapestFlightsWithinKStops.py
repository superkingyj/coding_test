from typing import List
import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for _src, _dst, price in flights:
            graph[_src].append((_dst,price))
        
        queue = [(0, src, -1)]
        visited = set()

        while queue:
            price, node, stop = heapq.heappop(queue)
            if stop > k: continue
            if node == dst: return price 
            if (price, node) in visited: continue
            visited.add((price, node))
            for v, w in graph[node]:
                alt = price + w
                print(f"heappush(queue, (alt: {alt} v:{v} stop:{stop+1})")
                heapq.heappush(queue, (alt, v, stop+1))
        return -1

sol = Solution()

# print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)==500)
# print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)==200)
# sol = Solution()
# print(sol.findCheapestPrice(4,[[0,3,59],[2,0,83],[2,3,32],[0,2,97],[3,1,16],[1,3,16]], 3, 0, 3))

print(sol.findCheapestPrice(13,
[[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]],
10,
1,
10))