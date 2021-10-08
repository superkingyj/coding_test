from collections import deque
import itertools

def moveTrucks(passingList):
    for item in passingList:
        item[1] -= 1

def getpassingTrucksWeight(passingList):
    return sum(item[0] for item in passingList)

def solution(bridge_length, weight, truck_weights):
    queue = deque(0 for _ in truck_weights)
    for i in range(len(truck_weights)):
        queue[i] = [truck_weights[i], bridge_length]

    time = 0
    passingList = deque([queue.popleft()])
    passedList = []

    while passingList:
        if passingList[0][1] <= 0:
            passingList.popleft()
        if queue and queue[0][0]+getpassingTrucksWeight(passingList) <= weight :
            truck = queue.popleft()
            passingList.append(truck)
            moveTrucks(passingList)
            time += 1
        else:
            moveTrucks(passingList)
            time += 1
    
    print(time)
    return time


print(solution(2,10,[7,4,5,6])==8)
print(solution(100,100,[10])==101)
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10])==110)

"""
트럭 속도 : 1초에 1칸
bridge_lenth : 다리 길이
weight : 다리 무제 제한

1. queue에 트럭의 무게와 다리의 길이를 튜플로 넣는다 
queue = deque((truck_weight, bridge_length) for truck in truck_weigths) 
2.  time = 0
    bridge_weight = 0
    while queue:
        if queue[0][1] <= 0: queue.popleft() --> 큐의 첫번째 트럭이 다리에 다 도착했을 경우
        else:
            if bridge_weight <= weight: --> 다리가 버틸수 있는 무게보다 적게 트럭이 올라가 있다면
                for item in queue:
                    item[1] -= 1
            time += 1
3. return time 

"""