class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        
        for i, char in enumerate(s):
            if char not in count:
                count[char] = [i, 1]
            else:
                count[char][1] += 1
            
        for k, v in count.items():
            if v[1] == 1:
                return v[0]
        
        return -1