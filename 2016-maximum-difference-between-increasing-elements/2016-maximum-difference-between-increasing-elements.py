class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = -1
        left, right = 0, 1
        while right < len(nums):
            if nums[left] < nums[right]:
                diff = nums[right] - nums[left]
                maxDiff = max(maxDiff, diff)
            else:
                left = right
            right += 1
        return maxDiff