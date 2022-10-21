class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_arr = []
        max_left = 0
        
        for i in height:
            max_left_arr.append(max_left)
            max_left = max(max_left, i)
        
        max_right_arr = []
        max_right = 0
        for j in range(len(height) - 1, -1, -1):
            max_right_arr.append(max_right)
            max_right = max(max_right, height[j])
        
        res = 0
        
        for k in range(len(height)):
            water_height = min(max_left_arr[k], max_right_arr[len(max_right_arr) - 1 - k])
            if water_height - height[k] > 0:
                res += (water_height - height[k])
                
        return res