class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float("inf")
        
        while l <= r:
            m = (l + r) // 2
            count = 0
            
            for num in piles:
                count += math.ceil(num/m)
                
                if count > h:
                    l = m + 1
                    break
            
            if count <= h:
                res = min(res, m)
                r = m - 1
                
        return res