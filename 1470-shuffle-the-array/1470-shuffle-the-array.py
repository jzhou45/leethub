class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        res = []
        
        while n < len(nums):
            res.append(nums[i])
            res.append(nums[n])
            i += 1
            n += 1
        
        return res