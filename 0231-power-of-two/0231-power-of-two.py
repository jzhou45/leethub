class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        pow2 = 2**count
        
        while pow2 <= n:
            if pow2 == n:
                return True
            count += 1
            pow2 = 2**count
        
        return False