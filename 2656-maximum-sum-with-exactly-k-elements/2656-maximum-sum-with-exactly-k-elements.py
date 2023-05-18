class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums) * k + sum([i for i in range(1, k)])