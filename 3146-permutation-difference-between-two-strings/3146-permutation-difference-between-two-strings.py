class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_dict = dict(zip(s, range(len(s))))
        t_dict = dict(zip(t, range(len(t))))
        
        res = 0
        for char in s:
            res += abs(s_dict[char] - t_dict[char])
        
        return res