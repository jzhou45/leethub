class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        t_dict = dict(zip(t, range(len(t))))

        res = 0
        for i, char in enumerate(s):
            res += abs(i - t_dict[char])
            
        return res