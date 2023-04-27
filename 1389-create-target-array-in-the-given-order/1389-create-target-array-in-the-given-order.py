class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            arr.insert(index[i], nums[i])
        return arr