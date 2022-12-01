class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        vowels = [0, 0, 0, 0, 0]
        
        while l < r:
            a = s[l].lower()
            b = s[r].lower()
            
            if a == "a":
                vowels[0] += 1
            elif a == "e":
                vowels[1] += 1
            elif a == "i":
                vowels[2] += 1
            elif a == "o":
                vowels[3] += 1
            elif a == "u":
                vowels[4] += 1
            
            if b == "a":
                vowels[0] -= 1
            elif b == "e":
                vowels[1] -= 1
            elif b == "i":
                vowels[2] -= 1
            elif b == "o":
                vowels[3] -= 1
            elif b == "u":
                vowels[4] -= 1
                
            l += 1
            r -= 1
        
        return sum(vowels) == 0