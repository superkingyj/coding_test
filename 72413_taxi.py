import collections
import heapq
import sys
from typing import *

'''
def solution(n, s, a, b, fares):
    answer = 0
    graph = makeGraph(fares)
    sToa, sTob = dijkstra(graph, s, a), dijkstra(graph, s, b)
    print(f"sToa : {sToa}, sTob: {sTob}")
    for i in range(1,n+1):
        if i==s: continue
        answer = min(sToa+sTob, dijkstra(graph,s,i)+dijkstra(graph,i,a)+dijkstra(graph,i,b))
        print(dijkstra(graph,s,i), dijkstra(graph,i,a), dijkstra(graph,i,b))
    print(answer)
    return answer
'''

class Graph:
    def __init__(self, n, fares):
        self.graph = self.makeGraph(fares)
        self.n = n

    def makeGraph(self, fares):
        graph = collections.defaultdict(list)
        for start, dst, cost in fares :
            graph[start].append((dst,cost))
            graph[dst].append((start,cost))
        return graph 

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

    def dijkstra(self, start):
        queue = [(0,start)]
#        visited = set()
        dist = collections.defaultdict(lambda : sys.maxsize)
        while queue :
            cost, node = heapq.heappop(queue)
            # if dist[node] < cost: continue
#            if (cost, node) in visited: continue
            if node not in dist:
#                visited.add((cost, node))
                dist[node] = cost
                for dst_, dst_cost in self.graph[node]:
                    heapq.heappush(queue, (cost + dst_cost,dst_))
        return dist

    def visitable_list(self, s):
        queue = [s]
        visited = set()
        while queue:
            node = queue.pop()
            visited.add(node)
            for dst, cost in self.graph[node]:
                if dst not in visited:
                    queue.append(dst)
        return list(visited)


graph = Graph(6, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
print(graph.dijkstra(5))
graph = Graph(7, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
print(graph.dijkstra(5))

print(graph.visitable_list(5))

graph = Graph(6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])
print(graph.dijkstra(6))
print(graph.visitable_list(2))

def solution(n, s, a, b, fares):
    graph = Graph(n, fares)
    fare_list = []
    for i in graph.visitable_list(s):
        dist_from_i = graph.dijkstra(i)
        fare_list.append(dist_from_i[s] + dist_from_i[a] + dist_from_i[b])
    return min(fare_list)

def solution(n, s, a, b, fares):
    answer = 0
    graph = makeGraph(fares)
    sToa, sTob = dijkstra(graph, s, a), dijkstra(graph, s, b)
    print(f"sToa : {sToa}, sTob: {sTob}")
    for i in range(1,n+1):
        if i==s: continue
        answer = min(sToa+sTob, dijkstra(graph,s,i)+dijkstra(graph,i,a)+dijkstra(graph,i,b))
        print(dijkstra(graph,s,i), dijkstra(graph,i,a), dijkstra(graph,i,b))
    print(answer)
    return answer


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])==82)
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])==14)
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])==18)
'''
Old Dij = O(V^2)
Q Dij = O(E log V)

n(V) = 200, n(n-1)/2 (E) = 20000
n * [Old Dij : O(40k)] = 8m
n * [Q Dij : O(20000 * 8) = O(160k)] = 32m
Floyd : 2.5s~5s (1.25s)
'''
