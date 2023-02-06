class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid = len(nums) // 2
        i = 0
        res = []
        
        while mid < len(nums):
            res.append(nums[i])
            res.append(nums[mid])
            i += 1
            mid += 1
        
        return res