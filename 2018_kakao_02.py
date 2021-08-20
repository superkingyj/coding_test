import re

def solution(dartResult):
    regexResult = re.split("(\d{1,2}\W{0,1})+", dartResult)[1:]
    strList = []
    for i in range(len(regexResult)):
        if i%2 == 0: str_ = regexResult[i]
        else : 
            str_ += regexResult[i]
            strList.append(str_)

    pointList = []
    for str in strList:
        point = int(re.split("(\D)+", str)[0])
        for i in range(len(str)):
            if str[i].isdigit(): continue
            elif str[i] == "S": point = pow(point,1)
            elif str[i] == "D": point = pow(point,2)
            elif str[i] == "T": point = pow(point,3)
            elif str[i] == "*": 
                point = point * 2
                if len(pointList) != 0: pointList[-1] = pointList[-1]*2
            else: point = point * -1
        pointList.append(point)    
    return sum(pointList)

print(solution("1S2D*3T")==37)
print(solution("1D2S#10S")==9)
print(solution("1D2S0T")==3)
print(solution("1S*2T*3S")==23)
print(solution("1D#2S*3S")==5)
print(solution("1T2D3D#")==-4)
print(solution("1D2S3T*")==59)