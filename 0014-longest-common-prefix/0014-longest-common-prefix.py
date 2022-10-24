class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        prefix = True
        
        while prefix and s != strs[0]:
            temp = s + strs[0][len(s)]
            for word in strs:
                if temp not in word[:len(temp)]:
                    prefix = False
                    break
            if prefix:
                s = temp
        
        return s