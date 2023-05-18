class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = {}
        
        for i, num in enumerate(nums):
            dic[num] = dic.get(num, []) + [i]
        
        res = 0
        
        for _, val in dic.items():
            if len(val) > 1:
                res += self.findGoodPairs(val, k)
        return res
    
    def findGoodPairs(self, arr, k):
        res = 0
        
        for i, num in enumerate(arr):
            for j in range(i + 1, len(arr)):
                if (num * arr[j]) % k == 0:
                    res += 1
        
        return res
            