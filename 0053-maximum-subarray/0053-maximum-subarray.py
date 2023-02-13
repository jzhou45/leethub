class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        curr_total = 0
        
        for num in nums:
            curr_total += num
            res = max(res, curr_total)
            
            if curr_total < 0:
                curr_total = 0
                
        return res