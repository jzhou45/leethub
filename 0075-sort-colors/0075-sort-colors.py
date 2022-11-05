class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        is_sorted = False
        
        while not is_sorted:
            is_sorted = True
            for i in range(len(nums) -1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    is_sorted = False