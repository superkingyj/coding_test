def solution(info, query):
    answer = []
    for q in query:
        count = 0
        for i in info:
            matchFalg = True
            for index, value in enumerate(q.replace("and", "").split(" ")):
                if value == "" or value == "-" : continue
                elif index == 7 and int(value) > int(i.split(" ")[-1]):
                    matchFalg = False
                    break
                elif index != 7 and value not in i.split(" "): 
                    matchFalg = False
                    break
            if matchFalg: count += 1
        answer.append(count)
    return answer

print(solution(
["java backend junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150",
"cpp backend senior pizza 260",
"java backend junior chicken 80",
"python backend senior chicken 50"],
["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"])==[1,1,1,1,2,4])

'''
1. make infoDictList --> [{language:~, job:~, career:~, food:~, grade:~} * len(info)]
2. put info into the dict
for infoDict, string in zip(infoDictList, info):
    infos = string.split(" ")
    infoDict["language"] = infos[0]
    infoDict["job"] = infos[1] ...
3. make quaryDictList --> [{language:~, job:~, career:~, food:~, grade:~} * len(quary)]
4. put quary into the dict
for quaryDict, string in zip(quaryDictList, quary):
    quarys = string.split(" ")
    quaryDict["language"] = quarys[0]
    quaryDict["job"] = quarys[1] ...
5. find infos match with quary
for quaryDict in quaryDictList:
    count = []
    matchFlag = True
    for infoDict in infoDictList:
        for key, value in quaryDict.items():
            if key == "grade" and value > infoDict[key]: break
            if value != infoDict[key]: break
            matchFlag = False
        if matchFlag: count += 1
    answer.append(count)
'''