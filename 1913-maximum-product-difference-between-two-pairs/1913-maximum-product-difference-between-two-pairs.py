class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        num1 = nums[-1] * nums[-2]
        num2 = nums[0] * nums[1]
        answer = num1 - num2
        return answer