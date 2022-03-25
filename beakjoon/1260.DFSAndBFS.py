import sys
from collections import defaultdict
from collections import deque

def BFS(n, m, v, graph, queue):
    visited = [v]
    queue.append(v)

    while queue:    
        v = queue.popleft()
    
        if v in graph.keys():
            for w in graph[v]:
                if w in visited:
                    continue
                visited.append(w)
                queue.append(w)
    
    return visited

def DFS(n, m, v, graph, visited):
    visited.append(v)

    if v in graph.keys():
        for w in graph[v]:
            if w in visited:
                continue
            DFS(n, m, w, graph, visited)
    
    return visited

if __name__ == "__main__":
    n, m, v = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)

    for _ in range(m):
        frm, to  = map(int, sys.stdin.readline().split())
        graph[frm].append(to)
        graph[to].append(frm)

    ## 정렬
    list_of_graph = sorted(graph.items(), key = lambda x: x[1])
    graph = dict(list_of_graph)
    [value.sort() for _, value in graph.items()]

    print(" ".join(map(str, DFS(n,m,v,graph,[]))))
    print(" ".join(map(str, BFS(n,m,v,graph,deque()))))

