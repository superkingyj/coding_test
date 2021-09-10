import collections
import heapq

def solution(n, edge):
    graph = collections.defaultdict(list)
    for v,w in edge:
        graph[v].append((w,1))
        graph[w].append((v,1))

    queue = [(0,1)]
    dist = collections.defaultdict(int)

    while queue :
        dst, node = heapq.heappop(queue)
        if node not in dist:
            dist[node] = dst
            for v,w in graph[node]:
                alt = dst + w
                heapq.heappush(queue, (alt,v))

    farthestDistance = 0
    for _, value in dist.items():
        farthestDistance = max(farthestDistance, value)

    return len([index for index, value in dist.items() if value == farthestDistance])


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])==3)