class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 if target == nums[0] else 0
    
        l, r = 0, 0
        res = float("inf")
        curr_sum = 0
        
        while r < len(nums):
            curr_sum += nums[r]
            if curr_sum >= target:
                res = min(r + 1 - l, res)
            while curr_sum > target and l < r:
                curr_sum -= nums[l]
                l += 1
                if curr_sum >= target:
                    res = min(r + 1 - l, res)
            r += 1
        
        return res if res != float("inf") else 0
            