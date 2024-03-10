class Solution:
    def reverseVowels(self, s: str) -> str:
        c, v = [], []
        
        vows = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
        for char in s:
            if char in vows:
                c.append(0)
                v.append(char)
            else:
                c.append(char)
        
        l = 0
        for r in range(len(c) - 1, -1, -1):
            if type(c[r]) == int:
                c[r] = v[l]
                l += 1
            
        return "".join(c)