class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr_count = max_count = 0
        
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        for i in range(k):
            if s[i] in vowels:
                curr_count += 1
        
        max_count = curr_count
        
        for j in range(1, len(s) - k + 1):
            temp_count = curr_count
            if s[j - 1] in vowels:
                temp_count -= 1
            if s[j + k - 1] in vowels:
                temp_count += 1
            max_count = max(max_count, temp_count)
            curr_count = temp_count
        
        return max_count