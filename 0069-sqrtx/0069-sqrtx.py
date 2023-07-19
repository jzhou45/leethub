class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        
        while True:
            if res * res == x: return res
            if res * res > x: return res - 1
            res += 1