class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        res = 0
        
        for char in s:
            if char in seen:
                res += 1
                seen = set()
            seen.add(char)
        
        if len(seen): res += 1
        return res