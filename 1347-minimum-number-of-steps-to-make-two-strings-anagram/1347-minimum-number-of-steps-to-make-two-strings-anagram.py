class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            count[char] = count.get(char, 0) -1
        
        res = 0
        for _, val in count.items():
            res += abs(val)
        
        return res//2