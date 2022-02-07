import collections
from collections import deque
from typing import Counter

def solution(priorities, location):
    prioritiesAndIndexs = deque()
    for index, priority in enumerate(priorities):
        prioritiesAndIndexs.append((priority, index))
    
    counter = 0
    while prioritiesAndIndexs:
        j = prioritiesAndIndexs.popleft()

        if prioritiesAndIndexs and max(prioritiesAndIndexs)[0] > j[0]:
            prioritiesAndIndexs.append(j)
            continue

        counter += 1
        if j[1] == location: return counter
    return -1
        
    
print(solution([2, 1, 3, 2], 2)==1)
print(solution([1, 1, 9, 1, 1, 1], 0)==5)
print(solution([1, 2, 3, 5, 9, 4], 2)==4)

# [(priority, index), ...]
# 0. priorities --> [(priority, index), ...]
# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# J = queue.popleft()
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# if J > max(queue.value()) --> queue.append(J)
# 3. 그렇지 않으면 J를 인쇄합니다.
# else --> print J

# prioritiesAndIndexs의 개수가 한개인 경우 max()연산에서 에러 발생, 예측 케이스가 1개인 경우 따져보기!