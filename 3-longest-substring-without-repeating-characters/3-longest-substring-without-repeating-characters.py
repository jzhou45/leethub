class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        longest = 0
        i = 0
        while i + longest < len(s):
            temp = s[i]
            for j in range(i + 1, len(s)):
                if s[j] not in temp:
                    temp += s[j]
                else:
                    longest = max(len(temp), longest)
                    break
            i += 1
            longest = max(len(temp), longest)
        return longest