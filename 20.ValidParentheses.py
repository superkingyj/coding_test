class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
                continue

            if not stack:
                return False

            elif char == ")" : 
                if "(" == stack.pop(): continue
                return False
            elif char == "}" :
                if "{" == stack.pop(): continue
                return False
            elif char == "]" :
                if "[" == stack.pop(): continue
                return False

        return False if stack else True

a = Solution()
print(a.isValid("()") == True)
print(a.isValid("()[]{}") == True)
print(a.isValid("(]") == False)
print(a.isValid("([)]") == False)
print(a.isValid("{[]}") == True)
        
# ( 를 보면 --> ) 스택에 넣기
# { 를 보면 --> } 스택에 넣기
# [ 를 보면 --> ] 스택에 넣기

# ) 를 보면 --> ( 를 비교 후 빼기, 없으면 False
# } 를 보면 --> { 를 비교 후 빼기, 없으면 False
# ] 를 보면 --> [ 를 비교 후 빼기, 없으면 False

# stack이 비었으면 True 반환, stack이 차있으면 False 반환


# )))

# ()((((
# 
# stack :

# ([)]
#
# stack : ([ --> False