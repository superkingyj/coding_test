class Solution:
    def __init__(self):
        self.memory = {}
        
    def fib2(self, n: int) -> int:
        if n in self.memory: return self.memory[n]
        val = 0
        if n < 2: val = n
        else: val = self.fib(n - 1) + self.fib(n - 2)
        self.memory[n] = val
        return val

    def fib(self, n: int) -> int:
        if n < 0: return 0
        memory = [0,1,1]
        for i in range(3,n+1):
            memory.append(memory[i-1]+memory[i-2])
        return memory[n]

# origin fibo 5 --> 3 4 --> 1 2, 2 3 --> -1 0, 0 1, 0 1, 1 2 : 15
# fibo 5 --> 3 4 --> 1 2 --> -1 0 : 7

# fibo 5 --> [0]:1 -> [1]:1 -> [2]:1+1 -> [3]:1+2 -> [4]:2+3 -> [5]:3+5
# fibo 1 1 2 3 5 8 13

# def fib(n)
#     if n<2: return n
#     return fib(n-1) + fib(n-2)


a = Solution()
print(f"fib(1) : {a.fib(1)}") # 0.05
print(f"fib(2) : {a.fib(2)}") # 0.05
print(f"fib(3) : {a.fib(3)}") # 0.05
print(f"fib(4) : {a.fib(4)}") # 0.05
print(f"fib(5) : {a.fib(5)}") # 0.05
print(f"fib(27) : {a.fib(27)}") # 0.05
print(f"fib(28) : {a.fib(28)}") # 0.
print(f"fib(29) : {a.fib(29)}") # 0.125
print(f"fib(30) : {a.fib(30)}") # 0.25
print(f"fib(31) : {a.fib(31)}") # 0.5
print(f"fib(32) : {a.fib(32)}") # 1
print(f"fib(33) : {a.fib(33)}") # 1
print(f"fib(34) : {a.fib(34)}") # 1

# Memorization

# 1K = 1024 == 2^10
# 1K*1K = 1024 * 1024 = 1M == 2^20
# 1G = 1024 * 1024 * 1024 = 2^30
# server : 1G compute per sec
# 2G

# O(2^n) n 10 --> 1K, n:20 --> (1K)^2
# 0 <= n <= 30