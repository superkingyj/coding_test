import collections
from types import coroutine

def solution(research, n, k):
    answer = ''
    reserchDict = collections.defaultdict(list)
    for i in range(len(research)): 
        reserchDict[i] = collections.Counter(research[i])
    
    issue = []

    for i in reserchDict.keys():
        for key, value in reserchDict[i].items():      
            if i+1 < len(reserchDict) and (value >= k) and (reserchDict[i+1][key] >= k) and (value + reserchDict[i+1][key] >= 2*n*k):
                issue.append(key)

    issueList = collections.Counter(issue)
    max_ = 0 
    result = []
    for key, value in issueList.items():
        max_ = max(max_, value)
        if max_ <= value: result.append(key)

    return sorted(result)[0]

# print(solution(["abaaaa","aaa","abaaaaaa","fzfffffffa"],2,2)=="a")
print(solution(["yxxy","xxyyy"],2,1)=="x")
print(solution(["yxxy","xxyyy","yz"],2,1)=="y")
print(solution(["xy","xy"],1,1)==None)