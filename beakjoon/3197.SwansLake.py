import sys
from collections import deque

def point_validation(x,y,r,c):
    if 0 <= x < c and 0 <= y < r:
        return True
    return False

def get_melt_list(ice, r, c):
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    melt_list = []
    visited = [[False for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if ice[i][j] == "ICE":
                for dir in dirs:
                    ny = dir[0] + i
                    nx = dir[1] + j
                    if point_validation(nx, ny, r, c) and (i,j) not in visited and (ice[ny][nx] == "WATER" or ice[ny][nx] == "SWAN"):
                        melt_list.append((i,j))
                        visited.append((i,j))
                        break
    return melt_list

def ice_melt(ice, melt_list):
    for melt_ice in melt_list:
        ice[melt_ice[0]][melt_ice[1]] = "WATER"

def two_swans_meet(ice, swans, r, c):
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    visited = [[False for _ in range(c)] for _ in range(r)]
    queue = deque()
    queue.append(swans[0])

    while queue:
        y, x = queue.popleft()
        visited[y][x] = True

        for dir in dirs:
            ny, nx = y + dir[0], x + dir[1]
            if point_validation(nx, ny, r, c) and not visited[ny][nx]:
                visited[ny][nx] = True
                if ice[ny][nx] == "SWAN":
                    return True
                elif ice[ny][nx] == "WATER":
                    queue.append((ny,nx))
        
    return False

def solv(ice, r, c, swans):
    day = 0
    while True:
        day += 1       
        melt_list = get_melt_list(ice, r, c)
        ice_melt(ice, melt_list)
        if two_swans_meet(ice, swans, r, c): 
            return day

if __name__ == "__main__":
    input = str(sys.stdin.readline())
    r, c = input.split()
    swans = []
    ice = [["WATER"] * int(c) for _ in range(int(r))]

    for i in range(int(r)):
        input = list(sys.stdin.readline().replace("\n", ""))
        for j in range(len(input)):   
            if input[j] == "X":
                ice[i][j] = "ICE"
            elif input[j] == "L":
                ice[i][j] = "SWAN"
                swans.append((i,j))

    print(solv(ice, int(r), int(c), swans))


"""
1. 얼음을 녹인다
전체 얼음의 위, 아래, 왼, 오를 탐색하면서 WATER인지 확인 후 WATER일 경우 melt_list에 append
방문한 곳은 또 방문하지 않도록 visited 관리
2. 백조1의 위치에서 백조2의 위치까지 가는 경로가 있는지 찾는다.
3. 경로가 존재할경우 return, 존재하지 않을경우 1부터 다시.

"""

"""
10 2
.L
..
XX
XX
XX
XX
XX
XX
..
.L
"""