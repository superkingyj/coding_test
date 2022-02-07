import string
import math
import collections

def convert(num, base) :
    tmp = string.digits+string.ascii_lowercase
    q, r = divmod(num, base)
    if q == 0: return tmp[r] 
    else: return convert(q, base) + tmp[r]

def isPrimeNum(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    convertToN = convert(n, k)
    numList = convertToN.split("0")
    counter = 0
    for num in numList:
        if num and isPrimeNum(int(num)):
            counter += 1
    return counter

print(solution(437674,3)==3)
print(solution(110011,10)==2)

# 1. n --> base convert --> nnnnnn
# 2. split --> list
# 3. prime check ()
# 234019238409812304981203948901283490120934809 -> 10 234019238409812304981203948901283490120934809
# dict memory[11] = true, memory[2] = true

'''
def convert(num, base) :
    tmp = string.digits+string.ascii_lowercase
    q, r = divmod(num, base)
    if q == 0: return tmp[r] 
    else: return convert(q, base) + tmp[r]

def isPrimeNum(n):
    if n == 0 or n == 1: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

def ifFormatPrimeNum(n):
    if n == "0": return 
    if len(n) >= 3:
        if n[0]=="0" and n[-1]=="0" and isPrimeNum(int(n)): return True
        return False
    if len(n) >= 3:
        if (n[0]!="0") and (n[-1]!="0") and "0" not in n and isPrimeNum(int(n)): return True
        return False
    if n[0]=="0" and isPrimeNum(int(n[1:])): return True
    if n[-1]=="0" and isPrimeNum(int(n[:-1])): return True

def solution(n, k):
    answer = 0
    number = str(convert(n,k))
    print(number)

    primeNums = set()
    for window in range(1, len(number)+1):
        for i in range(len(number)-window+1):
            windowNum = number[i:i+window]
            if isPrimeNum(int(windowNum)):
                if len(windowNum)==1 and number[i-1]=="0" and number[i+1]=="0" : primeNums.add(((i,i+window), windowNum))
                if len(windowNum) >= 3: 
                    if windowNum[0]=="0" and isPrimeNum(int(windowNum[1:])): primeNums.add(((i,i+window), windowNum))
                    if windowNum[-1]=="0" and isPrimeNum(int(windowNum[:-1])): primeNums.add(((i,i+window), windowNum))
                    primeNums.add(((i,i+window), windowNum))

    print(primeNums)

    for item in primeNums:
        if len(item[1])==1 and isPrimeNum(int(item[1])):
            answer += 1
            continue
        if "0" in item[1]:
            print(item[1][1:-1])
            if (item[1][0] == "0" or item[1][-1] == "0") and "0" not in item[1][1:-1]:
                answer += 1
        else :
            startIndex, endIndex, pnum = item[0][0]-1, item[0][1], item[1]
            if startIndex >= 0 and number[startIndex] == "0":
                answer += 1
                continue
            if endIndex < len(number) and number[endIndex]== "0":
                answer += 1
                continue

    return answer
'''