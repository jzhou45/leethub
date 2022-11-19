class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        
        l, r = 1, num // 2
        
        while l <= r:
            m = (l + r) // 2
            
            if m**2 == num:
                return True
            elif m**2 > num:
                r = m - 1
            else:
                l = m + 1
        
        return False