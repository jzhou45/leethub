class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        
        for i, n in enumerate(nums):
            right_sum -= n
            if right_sum == left_sum:
                return i
            left_sum += n
        return -1