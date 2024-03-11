class Solution:
    def removeStars(self, s: str) -> str:
        stars = 0
        res = ""
        
        i = len(s) - 1
        
        while i >= 0:
            if s[i] == "*":
                stars += 1
            elif stars == 0:
                res = s[i] + res
            else:
                stars -= 1
            i -= 1
        
        return res