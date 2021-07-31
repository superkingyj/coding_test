from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:

        if not heights :
            return 0
        
        result = 0
        left, right = 0, len(heights)-1
        leftTop, rightTop = heights[left], heights[right]

        while left < right :
            leftTop, rightTop = max(leftTop, heights[left]), max(rightTop, heights[right])
            if leftTop <= rightTop :
                result += leftTop - heights[left]
                left += 1
            else :
                result += rightTop - heights[right] 
                right -= 1             

        return result

a = Solution()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))


