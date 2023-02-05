class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {};
        for i in range(len(s)):
            if s[i] in letters:
                letters[s[i]] += 1
            else:
                letters[s[i]] = 1
        for j in range(len(t)):
            if t[j] in letters:
                letters[t[j]] += -1
            else:
                letters[t[j]] = -1
        for k in letters.values():
            if k != 0:
                return False
        return True