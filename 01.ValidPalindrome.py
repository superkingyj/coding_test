from typing import *
print("Hello world")

print("hi!")
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]", '', s)
        s.lower()
        return s == s[::-1]

    def isPalindrome2(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while True:
            if left == right: return True

            while(not s[left].isalnum() and left <= len(s)-1) :
                left += 1
 
            while(not s[right].isalnum() and right >= 0) :
                right -= 1
            
            if left >= right:
                break

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
                continue
            else:
                return False
        
        return True

a = Solution()
print(a.isPalindrome("race a car"))

# two pointer
# 1. left right
# 2. left -> LEFT, right -> RIGHT
# 3. loop
#       if left >= right return true
#       if
# 4.        left++, right-- , *left == *right -> continue
#       else
#           return false