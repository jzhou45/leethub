class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r = 0, len(p) - 1
        
        res = []
        count = Counter(p)
        
        while r < len(s):
            if Counter(s[l:r+1]) == count:
                res.append(l)
            l += 1
            r += 1
        
        return res
            