import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
data = list(map(int, input().split()))
result = 0

for i in range(1,n+1):
    lst = combinations(data,i)
    for lst_ in list(lst):
        if sum(lst_) == s: result += 1

print(result)
