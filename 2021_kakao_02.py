import collections
import itertools

def solution(orders, course):
    menu = []
    numberOfOrder = collections.defaultdict(int)
    for number in course:
        for order in orders: 
            for item in itertools.combinations(order, number):
                numberOfOrder["".join(sorted(item))] += 1
        values = [value for (key, value) in numberOfOrder.items() if len(key) == number]
        if not values: continue
        maxCount = max(values)
        for order, count in [(key, value) for (key, value) in numberOfOrder.items() if len(key) == number and value == maxCount and value >= 2]:
            menu.append(order)
    return sorted(menu)


# menu = []
# numberOfOrders = defaultdict(int)
# for number in course (2, 3, 4)
#     for item in 조합(order, length == number)
#         # item == AB, BA
#         numberOfOrders[sorted(item)] += 1
#
# for number in course (2,3,4)
#     numberOfOrders == {'AB':1, AC:2, ...., ABC: 1, ABF:1, ABG:1, ABCF:1, ABCG:1, ....}
#     for order, count in [(key, value) for key, value in enumerate(numberOfOrders) if len(key) == number]
#         if count < 2: continue
#         memu.append(order)
# return sorted(memu)


# ABC -> AB, AC, BC

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]) == ["AC", "ACDE", "BCFG", "CDE"])
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]) == ["ACD", "AD", "ADE", "CD", "XYZ"])
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]) == ["WX", "XY"])