from typing import *
from collections import deque
def solution(lines):
    answer = 0
    startTimeLogs = []
    endTimeLogs = []

    for line in lines :
        startTime, endTime = logToStarAndEndMillisec(line)
        startTimeLogs.append(startTime)
        endTimeLogs.append(endTime)
    
    startTimeLogs.sort()
    endTimeLogs.sort()

    startTimeLogs = deque(startTimeLogs)
    endTimeLogs = deque(endTimeLogs)

    _max = 0
    count = 0
    while True:
        print(f"count : {count}")
        print(startTimeLogs)
        print(endTimeLogs)

        if not startTimeLogs and not endTimeLogs:
            break
        
        if not startTimeLogs:
            endTimeLogs.popleft()
            count -= 1
            continue
        
        if startTimeLogs[0] - 999 <= endTimeLogs[0]:
            startTimeLogs.popleft()
            count += 1
            _max = max(_max, count)
        else:
            endTimeLogs.popleft()
            count -= 1

    return _max

# "2016-09-15 20:59:57.421 0.351s"
#  [0]            [1]       [2]
def logToStarAndEndMillisec(log: str) -> (int, int):
    _, startString, durationString = log.split()
    hh, mm, ss = startString.split(":")
    hh, mm, sssss, duration = int(hh), int(mm), int(float(ss)*1000), int(float(durationString[:-1])*1000)
    endTime = hh * 60 * 60 * 1000 + mm * 60 * 1000 + sssss
    startTime = endTime - (duration - 1)
    return (startTime, endTime)


# 1. log yy-mm-dd hh:mm:ss.sss duration --> (str)hh:mm:s* 60 s.sss to (int)start_millisec, (int)end_millisec--> start log, end log
# 2. start log, end log --> sort
# 3. return max processes per sec

print(solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))

print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))


print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))
