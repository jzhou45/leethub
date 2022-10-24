class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        res = [0] * len(height)
        
        while l != r:
            if max_right < max_left:
                r -= 1
                max_right = max(max_right, height[r])
                res[r] = max_right - height[r]
            else:
                l += 1
                max_left = max(max_left, height[l])
                res[l] = max_left - height[l]
        
        return sum(res)