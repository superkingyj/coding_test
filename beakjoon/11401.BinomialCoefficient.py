import sys
P = 1000000007

def power(a, b):
    if b == 0:
        return 1
    if b % 2:  
        return (power(a, b//2) ** 2 * a) % P
    else:
        return (power(a, b//2) ** 2) % P

def solve(N, K):
    fact = [1 for _ in range(N+1)]

    for i in range(2, N+1):
        fact[i] = fact[i-1] * i % P

    A = fact[N]
    B = (fact[N-K] * fact[K]) % P

    print((A % P) * (power(B, P-2) % P) % P )

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    solve(N,K)
