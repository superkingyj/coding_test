import collections
from typing import Collection

def solution(str1, str2):
    str1List = []
    str2List = []

    if not str1 and not str2 :
        return 65536

    for i in range(len(str1)):
        elem = str1[i:i+2]
        if elem.isalpha() and len(elem) > 1: 
            str1List.append(elem.upper())
    for i in range(len(str2)):
        elem = str2[i:i+2]
        if elem.isalpha() and len(elem) > 1: 
            str2List.append(elem.upper())

    if not str1List and not str2List :
        return 65536

    duplicateMin = 0
    duplicateMax = 0
    str1Count = collections.Counter(str1List)
    str2Count = collections.Counter(str2List)
    # str1Count'AA':3 'BB':2
    # str2Count'AA':5        'CC':1

    # {}.keys()
    # {}.values()
    # str1Count[key]
    for key in set(str1Count.keys()) | set(str2Count.keys()) :
        duplicateMin += min(str1Count[key], str2Count[key])
        duplicateMax += max(str1Count[key], str2Count[key])


    '''
    for elem, count in str1Count.items() :
        # elem : AA, BB
        if count > 1:
            if elem in str2Count : 
                # AA <- min OK
                duplicateMin += min(str1Count[elem], str2Count[elem])-1
                duplicateMax += max(str1Count[elem], str2Count[elem])-1

        # AA <- min OK
        
    # str1AndStr2 = set(str1List) | set(str2List)
    str1AndStr2 = len(str1Count) 
    str1OrStr2 = set(str1List) & set(str2List)
    '''
    # return int((len(str1OrStr2)+duplicateMin) / (len(str1AndStr2)+duplicateMax) * 65536)
    return int(duplicateMin / duplicateMax * 65536)

print(solution("FRANCE", "french")==16384)
print(solution("handshake", "shake hands")==65536)
print(solution("aa1+aa2", "AAAA12")==43690) 
print(solution("E=M*C^2", "e=m*c^2")==65536)