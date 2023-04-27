import numpy as np

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            curr_gcd = nums[i]
            for j in range(i,len(nums)):
                curr_gcd = np.gcd(curr_gcd, nums[j])
                if curr_gcd == k:
                    res += 1
                elif curr_gcd < k:
                    break
        return res