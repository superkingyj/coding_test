import collections
from bisect import bisect_left
from typing import Collection

# def solution(info, query):
#     # for i in info:
#     answer = []
#     for q in query:
#         count = 0
#         for i in info:
#             matchFalg = True
#             for index, value in enumerate(q.replace("and", "").split(" ")):
#                 if value == "" or value == "-" : continue
#                 elif index == 7 and int(value) > int(i.split(" ")[-1]):
#                     matchFalg = False
#                     break
#                 elif index != 7 and value not in i.split(" "): 
#                     matchFalg = False
#                     break
#             if matchFalg: count += 1
#         answer.append(count)
#     return answer


def ddict():
    return collections.defaultdict(ddict)

class DB:
    def __init__(self):
        # defaultdict in defaultdict # defaultdict of defaultdict
        self.database = ddict() #dictionary에 없는 새로운 key값을 조회하고 넣을때 사용 ddict()가 호출되어 defualtdict가 넣어진다

    def insert(self, info):
        # info : "python frontend senior chicken 210"
        # info : "python frontend senior chicken 110"
        _0, _1, _2, _3, score = info.split()
        if len(self.database[_0][_1][_2][_3]) == 0:
           self.database[_0][_1][_2][_3] = []
        self.database[_0][_1][_2][_3].append(int(score))
    
    def sort(self):
        for value1 in self.database.values():
            for value2 in value1.values():
                for value3 in value2.values():
                    for value4 in value3.values():
                        value4.sort()
    
    def __getdata(self, data, key):
        if key == "-":
            return data.values()
        return [data[key]]
    
    # 3
    # [1,2,2,2,3,3,3,3,3,3,4,4,4,5,6,8,8,8,8,8]
    def bSearch(self, list_, score):
        return bisect_left(list_, score)
    
    def get(self, query):
        # query : "- and backend and senior and - 150"
        _0, _1, _2, _3, score = query.replace(" and ", " ").split()
        score = int(score)
        sum_ = 0 
        for value1 in self.__getdata(self.database, _0):
            for value2 in self.__getdata(value1, _1):
                for value3 in self.__getdata(value2, _2):
                    for value4 in self.__getdata(value3, _3):
                        if len(value4) == 0: continue
                        sum_ += len(value4) - self.bSearch(value4, score)
        return sum_

def solution(info, query):
    db = DB()
    answer = []

    for _info in info:
        db.insert(_info)
    db.sort()

    for _query in query:
        answer.append(db.get(_query))
    
    return answer
    


'''
해당 문제 코드를 읽어보았는데, 시간 복잡도를 계산해보니 O(len(info) * len(query) * k) 이네요.
이경우 최선의 경우가 나와도 info가 50000, query가 100000 이라, 5G 번의 연산이 요구가 됩니다.
최소 5초 이상 걸린다는 것이라서 효율성에서 통과하지 못한 것 같아요.

? < O(n^2)
일단 1) info를 토대로 언어 상에서 데이터베이스를 구축하고, [O(n)] 2) query를 파싱해서 검색하도록 만들면 됩니다. [O(n log n)]

class DB:
    def __init__:
        self.database
    def insert(str):
        str parsing --> database[][][][].append(number)
    def sort():
        for item in database[][][][]
            item.sort()
    [5,10,15,30,70] --> 2 , 5 - bsearch(12)
    def _bsearch(list, 12): 12보다 크거나 같은 가장 왼쪽 인덱스 반환 

    def get(query): query에 해당하는 length
        total_count = 0
        for item in self.database[][][][]:
            _index = _bsearch(item, score)
            total_count += len(item) - _index
        return total_count


db = DB()

for i in info:
    db.insert(i)

db.sort()

answer = []
for q in query:
    answer.append(db.get(q))

return answer

1)을 하면 매 query 마다 info를 full scan 할일이 사라지니,
가능한 문자열 쿼리의 종류가 24종류니 찾아야 하는 정보가 1/24가 될 수 있습니다.
그런데, 2) 쿼리에서 점수로 range scan 을 요구로 하는 경우가 있는데,
해당 파트를 개선하지 않으면 결국 full scan과 동일한 시간복잡도를 가지게 됩니다.
이를 위해서는 이진 트리를 구현하거나, binary search를 구현해서 탐색 시간을 O(log n) 으로 줄여야 효율성을 통과할 수 있습니다!
'''

# database["-"]["backend"]["junior"]["pizza"] == list()
# databse["-"] --> database.values()
# {"k1":"value", "k2":"value"}
# -

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
