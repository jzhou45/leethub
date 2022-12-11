class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        count = set(nums)
        
        while original in count:
            original *= 2
        
        return original