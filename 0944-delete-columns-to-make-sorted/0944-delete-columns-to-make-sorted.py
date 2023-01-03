class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for i in range(len(strs[0])):
            prev = "a"
            for j in range(len(strs)):
                if strs[j][i] < prev:
                    res += 1
                    break
                prev = strs[j][i]
        return res
                