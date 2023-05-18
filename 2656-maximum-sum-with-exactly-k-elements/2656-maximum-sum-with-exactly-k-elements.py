class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        res = 0
        num = max(nums)
        for _ in range(k):
            res += num
            num += 1
        return res