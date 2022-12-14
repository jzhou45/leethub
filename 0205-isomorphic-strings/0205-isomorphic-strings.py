class Solution:
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        keys = {}
        values = {}
        
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            
            if s_char not in keys and t_char not in values:
                keys[s_char] = t_char
                values[t_char] = s_char
            elif s_char in keys and t_char in values:
                if keys[s_char] != t_char or s_char != values[t_char]: return False
            else:
                return False
        
        return True