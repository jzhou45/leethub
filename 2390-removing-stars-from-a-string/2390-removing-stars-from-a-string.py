class Solution:
    def removeStars(self, s: str) -> str:
        stars = 0
        res = ""
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "*":
                stars += 1
            elif stars == 0:
                res = s[i] + res
            else:
                stars -= 1
        
        return res