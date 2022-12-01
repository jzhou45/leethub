class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s)//2
        
        a = s[:half]
        b = s[half:]
        
        vowels = {"a":0, "e":0, "i":0, "o":0, "u": 0}
        
        for char in a:
            if char.lower() in vowels:
                vowels[char.lower()] += 1
        
        for char in b:
            if char.lower() in vowels:
                vowels[char.lower()] -= 1
        
        return sum(list(vowels.values())) == 0