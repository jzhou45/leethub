class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set([*allowed])
        res = 0
        for word in words:
            temp = True
            for char in word:
                if char not in allowed:
                    temp = False
                    break
            if temp:
                res += 1
        return res