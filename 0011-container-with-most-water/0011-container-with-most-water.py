class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = float("-inf")
        
        while left < right:
            width = right - left
            
            leftH, rightH = height[left], height[right]
            
            # figure out which pointer to move
            if leftH < rightH:
                left += 1
            else:
                right -= 1
            
            res = max(res, min(leftH, rightH) * width)
            
        return res