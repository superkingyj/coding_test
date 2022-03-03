import sys

def get_minimum_cost(n, m, bytes, costs):
    dp = [[0 for _ in range(sum(costs)+1)] for _ in range(n+1)]
    result = sum(costs)

    for i in range(1, n+1):
        byte = bytes[i]
        cost = costs[i]

        for j in range(1, sum(costs)+1):
            if j < cost:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j])
            if dp[i][j] >= m:
                result = min(result, j)
        
    if m!= 0: return result
    else: return 0

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    bytes = [0] + list(map(int, sys.stdin.readline().split()))
    costs = [0] + list(map(int, sys.stdin.readline().split()))
    print(get_minimum_cost(n, m, bytes, costs))