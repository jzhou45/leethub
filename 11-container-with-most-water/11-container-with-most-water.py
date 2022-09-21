class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        width = len(height) - 1
        res = 0
        while left < right:
            minNum = min(height[left], height[right])
            area = minNum * width
            if area > res:
                res = area
            if minNum == height[left]:
                left += 1
                width -= 1
                continue
            else:
                right -= 1
                width -= 1
        return res