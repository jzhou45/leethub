class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr_total = nums[0]
        
        for i in range(1, len(nums)):
            if curr_total < 0:
                curr_total = 0
                
            curr_total += nums[i]
            res = max(res, curr_total)
                
        return res