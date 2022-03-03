from itertools import permutations
import sys
from collections import deque

def bfs(w, h, room, positions):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    distance = [[0]  * w for _ in range(h)]
    q.append((positions[0], positions[1]))
    distance[positions[0]][positions[1]] = 1
    
    while q:
        x, y = q. popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if room[nx][ny] != "x" and not distance[nx][ny]:
                    distance[nx][ny] =  distance[x][y]+1
                    q.append((nx, ny))

    return distance

def get_minimum_clean_moves(w, h, room, dirty_count, robot_position, dirty_positions):
    distance = bfs(w, h, room, robot_position)

    robot_to_dirty = []

    for i, j in dirty_positions:
        if not distance[i][j]: 
            return -1
        robot_to_dirty.append(distance[i][j]-1)

    dirty_to_dirty = [[0]*dirty_count for _ in range(dirty_count)]
    
    for i in range(dirty_count-1):
        distance = bfs(w, h, room, (dirty_positions[i][0], dirty_positions[i][1]))
        for j in range(i+1, dirty_count):
            dirty_to_dirty[i][j] = distance[dirty_positions[j][0]][dirty_positions[j][1]]-1
            dirty_to_dirty[j][i] = dirty_to_dirty[i][j]

    permu = list(permutations([i for i in range(len(dirty_to_dirty))]))    
    minimum = sys.maxsize

    for i in permu:
        dist = 0
        dist += robot_to_dirty[i[0]]
        nfrom = i[0]
        for j in range(1, len(i)):
            nto = i[j]
            dist += dirty_to_dirty[nfrom][nto]
            nfrom = nto
        minimum = min(minimum, dist)
    
    return minimum

if __name__ == "__main__":
    while True:
        w, h = map(int, sys.stdin.readline().split())

        if not w and not h : break

        room = [["." for _ in range(w)] for _ in range(h)]
        dirty_count = 0
        robot_position = ()
        dirty_positions = []

        for i in range(h):
            input = list(sys.stdin.readline())
            for j in range(w):
                if input[j] == "x":
                    room[i][j] = "x"
                elif input[j] == "*":
                    room[i][j] = "*"
                    dirty_positions.append((i,j))
                    dirty_count += 1
                elif input[j] == "o":
                    robot_position = (i,j)

        print(get_minimum_clean_moves(w, h, room, dirty_count, robot_position, dirty_positions))
    

'''
1. realine(), count *
2. 다익스트라로 경로 저장
3. 최단 경로 찾아내기
4. *가 남아있으면 -1, 남아있지 안으면 최단경로 출력

7 5
.......
.o...*.
.......
.*...*.
.......
'''