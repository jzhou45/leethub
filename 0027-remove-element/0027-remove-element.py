class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        
        for i, num in enumerate(nums):
            if num != val:
                nums[idx] = nums[i]
                idx += 1
                
        return idx
