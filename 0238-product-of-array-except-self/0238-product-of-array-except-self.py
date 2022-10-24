from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = prod(nums)
        for i, num in enumerate(nums):
            if num == 0:
                temp = prod(nums[:i]) * prod(nums[i + 1:])
                res.append(temp)
            else:
                res.append(int(product / num))
        return res