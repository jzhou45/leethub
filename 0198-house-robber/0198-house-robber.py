class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in nums:
            temp = max(i + a, b)
            a = b
            b = temp
        return b