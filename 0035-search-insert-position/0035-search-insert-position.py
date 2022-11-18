class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        m = (l + r) // 2
        
        while l <= r:
            if nums[m] == target: return m
            
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
            
            m = (l + r) // 2
        
        return m + 1