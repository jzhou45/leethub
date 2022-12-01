class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        
        vowels = {"a":0, "e":0, "i":0, "o":0, "u": 0}
        
        while l < r:
            a = s[l].lower()
            b = s[r].lower()
            
            if a in vowels:
                vowels[a] += 1
            
            if b in vowels:
                vowels[b] -= 1
            
            l += 1
            r -= 1
        
        return sum(list(vowels.values())) == 0