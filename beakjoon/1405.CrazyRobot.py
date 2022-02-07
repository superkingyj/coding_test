import sys
global _map
global currentX
global currentY
global result
global percentage
_map = [[0] * 30 for _ in range(30)]
currentX, currentY, result, percentage = 15, 15, [], 1

def checkSimple(x,y):
    global _map
    if _map[x][y] == 1: return False
    _map[x][y] = 1
    return True

def move(N,e,w,s,n,cnt):
    global _map, currentX, currentY, result, percentage

    if cnt == N: 
        for i in result:
            percentage *= i
            result.pop()
        return True

    for i in (0,4):
       if i == 0: 
           if checkSimple(currentX+1,currentY):
               currentX = currentX+1
               result.append(e)
               move(N,e,w,s,n, cnt+1)
       elif i == 1: 
           if checkSimple(currentX-1,currentY):
                cnt += 1
                currentX = currentX-1
                result.append(w)
                move(N,e,w,s,n)
       elif i == 2: 
            if checkSimple(currentX,currentY+1):
                cnt += 1
                currentY = currentY+1
                result.append(w)
                move(N,e,w,s,n)
       else :
           if checkSimple(currentX,currentY-1):
               cnt += 1
               currentY = currentY-1
               result.append(n)
               move(N,e,w,s,n)

    percentage = 1
    for i in result:
        percentage = percentage * i
    print(f'%0.9f' % percentage)
    exit()  

if __name__ == "__main__":
    input = sys.stdin.readline  
    N, e, w, s, n = input().split()
    move(int(N), int(e)*0.01, int(w)*0.01, int(s)*0.01, int(n)*0.01, 0)
