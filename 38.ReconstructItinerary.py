from typing import List
import collections
from collections import deque


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for from_, to_ in tickets:
            graph[from_].append(to_)
        for from_ in graph:
            graph[from_] = deque(sorted(graph[from_]))

        visited = []
        stack = ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].popleft())
            visited.append(stack.pop())
        return visited[::-1]

'''
        visited = [Solution.FIRST_PLACE]
        place = Solution.FIRST_PLACE

        stack = [Solution.FIRST_PLACE]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].popleft())
            visited.append(stack.pop())
        return visited[::-1]

        while True:
            print(f"place : {place}, graph[{place}]: {graph[place]}")
            if not graph[place]: 
                break
            place = graph[place].popleft()
            visited.append(place)
        return visited
'''

Solution.FIRST_PLACE = 'JFK'

# [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]



# Building Graph
# ticket = [(from to) * n]
# graph[from] = [] <-- graph[from].append(to)

# for every from : graph[from].sort()
# aaaa bbb cc
# smallest --> aaaa bbb cc
# largest --> cc bbb aaaa

# visited = ['JFK']
# place = 'JFK'
# while True
#     if is_visitable(place)
#         place = graph[place].popleft() <-- deque
#         visited.append(place)
#     break
# for every visited places : visited.apppend(visited_place)

# return visited


a = Solution()
print(a.findItinerary(tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
print(a.findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(a.findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))