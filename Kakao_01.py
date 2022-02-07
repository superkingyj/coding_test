from typing import Collection


import collections
def solution(id_list, report, k):
    answer = []
    ## id별 신고한 id 목록
    reportDict = collections.defaultdict(set)
    ## id별 신고 당한 횟수
    reportedCount = collections.defaultdict(set)
    for item in report:
        i,j = item.split(" ")[0], item.split(" ")[1]
        reportDict[i].add(j)
        reportedCount[j].add(i)

    print(f"reportDict : {reportDict}")
    print(f"reportedDict :  {reportedCount}")

    bandedList = []
    for key, value in reportedCount.items():
        if len(value) >= k: bandedList.append(key)
    
    for id in id_list:
        mailCount = 0 
        for i in reportDict[id]:
            if i in bandedList: mailCount+= 1
        answer.append(mailCount)

    print(answer)
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],
["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)==[2,1,1,0])
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"],3)==[0,0])
