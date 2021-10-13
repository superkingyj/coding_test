import sys
from itertools import combinations

input = sys.stdin.readline
l, c = map(int, input().split())
data = list(input().split())
vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
results = []

cobi = combinations(data,l)
for item in list(cobi):
    vCount = 0 
    cCount = 0 

    print(item)
    for vowel in vowels :
        if vowel in item: vCount += 1
    for consonant in consonants:
        if consonant in item: cCount += 1
    if vCount >= 1 and cCount >= 2: 
        item = sorted(item)
        results.append("".join(item))

results.sort()
for result in results:
    print(result)