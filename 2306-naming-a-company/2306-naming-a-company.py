class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        alphabet = [set() for _ in range(26)]
        
        for idea in ideas:
            # ord(idea[0]) grabs unicode for first letter, subtracting it
            # by ord("a") returns the index in the alphabet arr associated with
            # the first letter
            alphabet[ord(idea[0]) - ord('a')].add(idea[1:])
        
        ans = 0
        
        for i in range(25):
            for j in range(i + 1, 26):
                k = len(alphabet[i] & alphabet[j]) # Number of duplicated suffixes
                ans += 2 * (len(alphabet[i]) - k) * (len(alphabet[j]) - k)
                
        return ans