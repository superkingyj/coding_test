class Solution:
    def trap(self, height: List[int]) -> int:

        if not height :
            return 0
        
        result = 0
        left, right = 0, len(height)-1
        leftMax, rightMax = height[left], height[right]

        while left < right :
            leftMax, rightMax = max(leftMax, height[left]), max(rightMax, height[right])
            if leftMax <= rightMax :
                result += leftMax - height[left]
                left += 1
            else :
                result += rightMax - height[right] 
                right -= 1             

        return result