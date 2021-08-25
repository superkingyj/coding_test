def solution(n, t, m, timetable):
    timetable = [
        int(time[:2]) * 60 + int(int(time[3:]))
        for time in timetable
    ]
    timetable.sort()

    current = 540

    for _ in range(n):
        for _ in range(m):
            if timetable and timetable[0] <= current:
                candidate = timetable.pop(0)-1
            else : candidate = current
        current += t
    
    h,m = divmod(candidate, 60)
    return str(h).zfill(2) + ":" + str(m).zfill(2)

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])=="09:00")
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"])=="09:09")
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])=="08:59")
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])=="00:00")
print(solution(1, 1, 1, ["23:59"])=="09:00")
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])=="18:00")

'''
ex1) 09:00 / 5명 / ["08:00", "08:01", "08:02", "08:03"] --> 09:00
ex2) 09:00, 09:10 / 2명 / ["09:10", "09:09", "08:00"] -->  09:09
ex3) 09:00, 09:01 / 2명 / ["09:00", "09:00", "09:00", "09:00"] --> 08:59
ex6) 09:00, 10:00 ... 18:00 / 45명 / [] --> 18:00 

1. timetable 배열 안의 문자열에 포함된 ":" 지우기
-> timetable = stack(list(int(item.replace(":", "")) for item in timetable).sorted())

2. 마지막 버스 도착 시간을 구해서 그 이후에 도착한 크루들 지우기
-> lastBusArrivedTime = 0900 + t * n
10, 60, 45 -> 9:00 + 10(n-1) * 60(t) / 60 * 100 -> 18:00
for item in timetable: if item > lastBusArrivedTime: timetable.remove(item)

3. if not timetable: return str(lastBusArrivedTime[0:2]) + ":" + str(lastBusArrivedTime[2:])

4. 
for i in range(n):
    busArrivedTime, cruesNum = 900 + (t*n), m
    while cruesNum: ## 탈 수 있는 사람이 남았음
        ## 탈 수 있는 사람은 남았는데 timetable에 아무도 없는 경우
        if not timetable: return busArrivedTime
        ## 탈 수 있는 사람도 남았고 timetable에 도착시간 내의 사람이 있는 경우
        elif timetable[0] <= busArrivedTime: timetable.pop(0)
        ## 탈 수 있는 사람이 남았는데 timetable에 도착시간 내의 사람이 없는 경우
        else: return busArrivedTime
    ## 탈 수 있는 사람이 없음

'''