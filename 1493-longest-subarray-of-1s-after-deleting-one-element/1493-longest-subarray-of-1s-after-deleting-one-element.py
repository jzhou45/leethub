class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        last_zero = -1
        curr_max = 0
        curr_sum = 0
        
        for i, num in enumerate(nums):
            if num == 1:
                curr_sum += 1
            elif last_zero == -1:
                last_zero = i
            else:
                temp_sum = i - last_zero - 1
                curr_max = max(temp_sum, curr_max, curr_sum)
                curr_sum = temp_sum
                last_zero = i
        
        return max(curr_sum, curr_max) - (1 if last_zero == -1 else 0)