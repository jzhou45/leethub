class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1

        s1 = sorted(s1)

        while r < len(s2):
            temp = s2[l:r + 1]
            temp = sorted(temp)

            if s1 == temp: return True
            
            l += 1
            r += 1
        
        return False