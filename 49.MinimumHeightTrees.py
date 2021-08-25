from typing import List
import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1 : return [0]

        graph = collections.defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        while True:
            if len(graph) <= 2 : return list(graph.keys())

            leafNodes = []
            for key in graph.keys():
                if len(graph[key]) <= 1: leafNodes.append(key)
            
            for node in leafNodes:
                graph[graph[node][0]].remove(node)
                del graph[node]
            
    
sol = Solution()
# print(sol.findMinHeightTrees(4,[[1,0],[1,2],[1,3]])==[1])
# print(sol.findMinHeightTrees(6,[[3,0],[3,1],[3,2],[3,4],[5,4]])==[3,4])
# print(sol.findMinHeightTrees(1,[])==[0])
# print(sol.findMinHeightTrees(2,[[0,1]])==[0,1])
print(sol.findMinHeightTrees(6,[[0,1],[0,2],[0,3],[3,4],[4,5]])==[3])
