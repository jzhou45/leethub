class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i= 0
        m = ""
        
        while i < len(word1) and i < len(word2):
            m += word1[i] + word2[i]
            i += 1
        
        m += word1[i:] + word2[i:]
        
        return m