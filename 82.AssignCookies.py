from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_index, cookies_index, child = 0,0,0
        while cookies_index < len(s) and child_index < len(g):
            if g[child_index] <= s[cookies_index] : 
                child += 1
                child_index +=1
                cookies_index += 1
            else : 
                cookies_index += 1
        return child
        

sol = Solution()
print(sol.findContentChildren([1,2,3],[1,1])==1)
print(sol.findContentChildren([1,2],[1,2,3])==2)

'''
g : [1,2,3]
s : [1,1]
child : 쿠키를 받은 아이
index 0 : g[0] <= s[0] --> child++
index 1 : g[1] > s[1]
index 2 :
'''