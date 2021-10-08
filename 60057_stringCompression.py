from typing import Pattern
import sys

import collections 

def printDict(patternCountDict):
    for index, value in patternCountDict.items():
        print(f"{index} : {value}")

def solution(s):
    unit = 1
    patternCountDict = collections.defaultdict(list)

    while unit <= len(s):
        pattern = None
        pointer = 0
        patternCount = 0
        for index in range(unit, len(s)+1, unit):
            if not pattern:
                pattern = s[pointer:index]
            if pattern == s[pointer:index]: pass
            else :
                patternCountDict[unit].append((pattern, patternCount))
                pattern = s[pointer:index]
                pointer = index
                patternCount = 1
                continue
            pointer = index
            patternCount +=1
        
        patternCountDict[unit].append((pattern, patternCount))
        if index < len(s):
            patternCountDict[unit].append((s[index:], 1))
        unit += 1


    minStringLength = sys.maxsize
    for _, value in patternCountDict.items():
        str_ = ""
        for char, charCount in value:
            if charCount <= 1: 
                str_ = str_ + char
                continue
            str_ = str_ + str(charCount) + char
        minStringLength = min(minStringLength, len(str_))

    return minStringLength


print(solution("aabbaccc")==7)
print(solution("ababcdcdababcdcd")==9)
print(solution("abcabcdede")==8)
print(solution("abcabcabcabcdededededede")==14)
print(solution("xababcdcdababcdcd")==17)


'''
aabbaccc -> 1개단위 : 2a2ba3c -> 7
ababcdcdababcdcd -> 8개단위 : 2ababcdcd -> 9
abcabcdede ->  3개단위 : 2abc2de -> 7
abcabcabcabcdededededede -> 6개단위 : 2abcabc2dedede -> 14
xababcdcdababcdcd -> 제일 앞부터 정해진 길이대로 잘라야하므로 압축x

1.len(s) --> 문자열을 자를 수 있는 범위 1~len(s)
2.
unit = 1
pattern = none
pointer = 0
patternCount = 0
patternCountList = defaultDict(list) --> [[1]: [('a',2), ('b',2), ('a', 1), ('c',3)], -> 2a2ba3c
                           [2]: [('aa',1), ('bb',1), ('ac',1), ('cc',1)]] -> aabbaccc
while(unit <= len(s)):
    for index in range(0, len(s), unit):
        if not pattern : --> 처음 for문 진입했을 경우
            pattern = s[pointer:index]
            pointer = index
            pattenrCount += 1
            continue
        if pattern == s[pointer:index]  --> pattern과 일치하는 경우
            pointer = index
            patternCount += 1
            continue 
        else : --> pattern과 일치하지 않는 경우
            patternCount[unit].append((pattern, patternCount))
            pattern = s[pointer:index]
            pointer = index
            patternCount +=1
    unit += 1

minStringLength = 100000000000
for _, value enum(patternCountList):
    for char, charCount in value:  
        minStringLength = min(minStringLength,len("".join(str(charCount),char)))

return minStringLength
'''
