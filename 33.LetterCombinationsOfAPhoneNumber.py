from typing import *
from itertools import combinations

class Solution:
    def __init__(self):
        self.digit_letters = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

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

    def letterCombinations(self, digits: str) -> List[str]:
        return self.combinations(digits, [])

sol = Solution()
print(sol.letterCombinations(""))
print(sol.letterCombinations("2"))
print(sol.letterCombinations("23"))
print(sol.letterCombinations("234"))

# def combinations("2", ? ?) --> ["a","b","c"]
# def combinations("23", ? ?) --> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# def combinations("234", ? ?) --> ["ad*" * 27]

# case2
# def combinations(digits, register)
# def combinations("23", []) --> combinations("3", ["a","b","c"])
# def combinations("3", ["a","b","c"]) --> combinations("", ["ad","ae","af","bd","be","bf","cd","ce","cf"])
# def combinations("", ["ad","ae","af","bd","be","bf","cd","ce","cf"]) -> ["ad","ae","af","bd","be","bf","cd","ce","cf"] 

# 1. digits 에서 앞 1글자 char 가져오기
# 2. char에 해당하는 letters 가져오기 2 --> abc
# 3. tmp_register = []
# 3. for item in register
# 4.     tmp_register += [item+letter for letter in letters]
# 5. return combinations(digits[1:], tmp_register)

# digit -> chars, 2->abc