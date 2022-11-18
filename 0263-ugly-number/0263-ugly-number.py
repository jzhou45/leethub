class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1: return False
        
        divideable = True        
        
        while divideable:
            if n == 1:
                break
            
            if n % 2 == 0:
                n /= 2
            elif n % 3 == 0:
                n /= 3
            elif n % 5 == 0:
                n /= 5
            else:
                return False
            
        return True