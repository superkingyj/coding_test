import sys

result = []

def checkSequence(rst):
    if len(rst) <= 1: return True
    length = len(rst)-1
    rst = "".join(rst)
    for i in range(1,len(rst)//2+1): 
        x = rst[len(rst)-i:len(rst)]
        y = rst[length-i:len(rst)-i]
        if x == y: return False
        length -= 1     
    
    return True

def makeSequence(n):
    if len(result) == n: 
        print("".join(result))
        exit()
        
    for i in range(1,4):
        tmp = result.copy()
        tmp.append(str(i))
        if checkSequence(tmp):
            result.append(str(i))
            makeSequence(n)
            result.pop()

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    makeSequence(n)


'''
121" " -> 4번째 인덱스 결정
1. 1211 -> 1(3) == 1(4) -> x
2. 1212 -> 1(3) != 2(4) -> o
        -> 12(1,2) == 12(3,4) -> x
3, 1213 -> 1(3) != 3(4) -> o
        -> 12(1,2) != 13(3,4) -> o


'''
