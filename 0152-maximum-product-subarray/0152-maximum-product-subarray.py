class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1
        
        for num in nums:
            temp = curr_max * num
            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(temp, num * curr_min, num)
            res = max(curr_max, res)
            
        return res
            
        