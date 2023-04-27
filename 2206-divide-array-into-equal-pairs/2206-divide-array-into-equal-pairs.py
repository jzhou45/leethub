class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        for idx in range(0, len(nums), 2):
            if nums[idx] != nums[idx + 1]:
                return False
        return True