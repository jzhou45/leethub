class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(t) == 0: return False
        
        if s[0] == t[0]:
            return self.isSubsequence(s[1:len(s)], t[1:len(t)])
        else:
            return self.isSubsequence(s, t[1:len(t)])