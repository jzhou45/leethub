class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        
        if len(pattern) != len(s): return False
        
        char_to_word = {}
        word_to_char = {}
        
        for i in range(len(pattern)):
            if pattern[i] not in char_to_word:
                char_to_word[pattern[i]] = s[i]
            if s[i] not in word_to_char:
                word_to_char[s[i]] = pattern[i]
            if char_to_word[pattern[i]] != s[i] or word_to_char[s[i]] != pattern[i]:
                return False
        return True