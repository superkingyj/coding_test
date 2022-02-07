from collections import deque
import collections

def findSameJobNum(queue, jobNum):
    sameJobNumList = []
    for item in queue:
        if jobNum == item[2]: sameJobNumList.append(item)

    if sameJobNumList: 
        for item in queue:
            for i in sameJobNumList:
                if item == i : queue.remove(item)
        return sameJobNumList
    return None

def findNextJob(queue):
    nextJob = collections.defaultdict(int)
    jobList = collections.defaultdict(list)
    for item in queue:
        nextJob[item[2]] += item[3]
        jobList[item[2]].append(item)
    
    next = []
    max_ = 0
    for key, value in nextJob.items():
        if value >= max_ :
            max_ = value
            next.append((key, value))
    
    if next :
        num = sorted(next)[0][0]
        for item in queue:
            if item == jobList[num][0] : queue.remove(item)
        return jobList[num][0]
    return False

def solution(jobs):
    answer = set()
    jobDict = collections.defaultdict(list)
    for job in jobs:
        jobDict[job[0]] = job
    
    time = 1
    queue = []
    queue.append(jobDict[1])
    processingWork = queue.pop(0)
    
    while processingWork:
        jobTime, jobNum, jobImportance = processingWork[1], processingWork[2], processingWork[3]    
        answer.add(jobNum)
        while jobTime > 0:
            if time in jobDict.keys() and jobDict[time] != processingWork: queue.append(jobDict[time])
            time +=1
            jobTime -= 1

        if time in jobDict.keys() and jobDict[time] != processingWork: queue.append(jobDict[time])

        sameJob = findSameJobNum(queue, jobNum)
        if sameJob: processingWork = sameJob.pop(0)
        else: processingWork = findNextJob(queue)  

    return list(answer)

print(solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]])==[2, 1, 2, 3])
print(solution([[1, 2, 1, 5], [2, 1, 2, 100], [3, 2, 1, 5], [5, 2, 1, 5]])==[1, 2])
print(solution([[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]])==[3,4])
print(solution([[0, 5, 1, 1], [2, 4, 3, 3], [3, 4, 4, 5], [5, 2, 3, 2]])==[1, 3, 4])