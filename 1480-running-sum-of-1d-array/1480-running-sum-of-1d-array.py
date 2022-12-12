class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr = 0
        for num in nums:
            curr += num
            yield curr