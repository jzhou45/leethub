class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        r = 0
        poss_farthest = 0
        for i in range(len(nums) - 1):
            poss_farthest = max(poss_farthest, i + nums[i])
            if i == r:
                jumps += 1
                r = poss_farthest
        return jumps