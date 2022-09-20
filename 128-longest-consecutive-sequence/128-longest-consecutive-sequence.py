class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        cons = []
        temp = 1
        for i in range(len(nums) -1):
            if nums[i + 1] == nums[i] + 1:
                temp += 1
            elif nums[i + 1] == nums[i]:
                continue
            else:
                cons.append(temp)
                temp = 1
        cons.append(temp)
        cons.sort()
        return cons[len(cons) - 1]