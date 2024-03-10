class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = res = sum(nums[:k])
        
        for i in range(1, len(nums) - k + 1):
            temp_sum = curr_sum - nums[i - 1] + nums[i + k - 1]
            res = max(res, temp_sum)
            curr_sum = temp_sum

        return res/k