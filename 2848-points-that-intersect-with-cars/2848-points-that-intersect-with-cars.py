class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        res = set()
        
        for subarr in nums:
            i, j = subarr
            res = res.union(set(range(i, j + 1)))
            
        return len(res)