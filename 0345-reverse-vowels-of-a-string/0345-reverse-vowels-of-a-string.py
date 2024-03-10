class Solution:
    def reverseVowels(self, s: str) -> str:
        c, v = [], []
        
        vows = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
        for i, char in enumerate(s):
            if char in vows:
                c.append(i)
                v.append(char)
        
        s = list(s)
        for j in range(len(c) - 1, -1, -1):
            s[c[j]] = v[len(c) - j - 1]
        
        return "".join(s)