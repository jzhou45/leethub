class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 3 and n != 1:
            return False
        
        if n == 3 or n == 1:
            return True
        
        return self.isPowerOfThree(n / 3)