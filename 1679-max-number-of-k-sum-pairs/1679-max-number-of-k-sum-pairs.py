class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = {}
        res = 0
        
        for n in nums:
            r = k - n
            if r in dic and dic[r] > 0:
                res += 1
                dic[r] -= 1
            else:
                dic[n] = dic.get(n, 0) + 1
        
        return res