class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        res = []
        for i in range(len(s) - 1, -1, -1):
            if len(s[i]) > 0:
                res.append(s[i])
        return " ".join(res)
            