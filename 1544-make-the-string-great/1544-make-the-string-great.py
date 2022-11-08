class Solution:
    def makeGood(self, s: str) -> str:
        great = False
        
        while not great:
            great = True
            for i in range(len(s) - 1):
                if s[i] == s[i].lower() and s[i + 1] == s[i].upper() \
                or s[i] == s[i].upper() and s[i + 1] == s[i].lower():
                    s = [*s]
                    a, b = s[:i], s[i + 2:]
                    s = a + b
                    s = "".join(s)
                    great = False
                    break
        
        return s