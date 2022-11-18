class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 1
        res = 0
        
        while n > 0:
            n -= count
            count += 1
            res += 1
        
        return res - 1 if n < 0 else res