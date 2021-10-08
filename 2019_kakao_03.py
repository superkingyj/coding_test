import itertools
import copy

def getPossibleKeys(column_len):
    combi = []
    for i in range(1,column_len+1):
        for tuple_ in itertools.combinations(range(column_len),i):
            print(tuple_)
            combi.append(tuple_)
    return combi

def lookupByKey(relation, key):
    datas = []
    print(key)
    for row in relation:
        data = []
        for k in key:
            data.append(row[k])
        # (rayn, music)
        datas.append(tuple(data))
    return datas

def doesLargeKeyContainsSmallKey(largeKey, smallKey):
    # largeKey 가 smallKey 를 포함하면 return True
    # largeKey = (1,2,3)
    # smallKey = (1,2,3,4)
    for key in smallKey:
        if key not in largeKey:
            return False 
    return True

def getMinimumKeys(uniquenessKeys):
    print(f'before: {uniquenessKeys}')
    tmp = copy.copy(uniquenessKeys)
    for key in uniquenessKeys:
        # key == (0,) or (1,2,)
        for item in tmp:
            if key == item: continue
            print(f'key, item : {key}, {item}')
            if doesLargeKeyContainsSmallKey(item, key) and item in uniquenessKeys:
                uniquenessKeys.remove(item)
    print(f'after: {uniquenessKeys}')
    return uniquenessKeys


def solution(relation):
    row_len = len(relation)
    column_len = len(relation[0])

    # 유일성
    # 3 -> 0,1,2,(0,1),(0,2),(1,2),(0,1,2)
    keys = getPossibleKeys(column_len)
    uniquenessKeys = []
    for key in keys:
        datas = lookupByKey(relation, key) # key==0 --> [(100), (200), (300), (400)] or [(ryan, music), (apeach, match)]
        set_ = set()
        for data in datas:
            set_.add(data)
        if len(set_) == row_len:
            uniquenessKeys.append(key)
    print(uniquenessKeys)

    # 최소성
    return len(getMinimumKeys(uniquenessKeys))

'''
유일성 체크
학번, (이름, 전공) --> 조합으로 다 꺼내오기

set(학번) 
len(set) == len(relation) --> 학번은 후보키
set.add((이름, 전공))
len(set) == len(relation) --> 이름, 전공 후보키

최소성 체크
학번, (학번, 이름), (학번, 전공), (이름, 전공), ...
'''

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]) == 2)
print(solution([["100","ryan","music","4"],
                ["100","ryan","music","5"]]) ==  1)