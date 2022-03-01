import sys
## 피보나치 수를 나눌 수. 10^6
M = 1000000 
## 주기의 길이. 15*10(6-1)
P = 15*pow(10,5)

def get_fibonacci_number(N:int):
    fibo = [0,1]
    for i in range(2, P):
        fibo.append(fibo[i-2]+fibo[i-1])
        fibo[i] %= M
    return(fibo[N%P])

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    print(get_fibonacci_number(N))