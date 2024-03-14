class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = {}
        curr_sum = 0
        res = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]

            if (curr_sum - goal) in prefix:
                res += prefix[curr_sum - goal]
                
            if curr_sum == goal:
                res += 1
                
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            
        return res