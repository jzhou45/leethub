class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {};
        
        for char in s:
            letters[char] = letters.get(char, 0) + 1
                
        for char2 in t:
            if char2 not in letters:
                return False
            else:
                letters[char2] -= 1
                
        for k in letters.values():
            if k != 0:
                return False
            
        return True