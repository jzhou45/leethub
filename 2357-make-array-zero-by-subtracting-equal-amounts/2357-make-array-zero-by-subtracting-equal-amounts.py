class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        
        nums = set(nums)
        
        if 0 in nums:
            nums.remove(0)
        
        return res + len(nums)