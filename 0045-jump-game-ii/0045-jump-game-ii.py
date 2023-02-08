class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        end = 0
        maxPosition = 0
        for i in range(len(nums) - 1):
            maxPosition = max(maxPosition, i + nums[i])
            if i == end:
                step += 1
                end = maxPosition
        return step