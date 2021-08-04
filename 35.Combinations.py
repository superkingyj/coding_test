class Solution:
    def combinations(self, digits, register:List[str]):
        if not digits:
            return register

        letters = self.digit_letters[digits[0]]

        if not register:
            return self.combinations(digits[1:], [letter for letter in letters])

        tmp_register = []
        for item in register:
            tmp_register += [item+letter for letter in letters] 

        return self.combinations(digits[1:], tmp_register)

    def combine(self, n: int, k: int) -> List[List[int]]:
        pass

# def combination(numbers, register, k <-- (len))
# combination([1,2,3], [], 2) --> combination([2,3], [1], 1) + combination([3], [2], 1) + combination([], [3], 1)
# combination([2,3], [1], 1) --> combination([3], [1,2], 0)

# def combination(4, ??) -> [??, 4], [??, 4] -> 4-1
# def combination(3, ??) -> [??, 3], 

sol = Solution()
print(sol.combine(n = 4, k = 2))
'''
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''

print(sol.combine(n = 1, k = 1))
'''
[[1]]
'''
