class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n <= 2:
            return n - 1
        
        if n % 2 == 0:
            return n // 2 + self.numberOfMatches(n // 2)
        else:
            return (n - 1) // 2 + self.numberOfMatches((n - 1) // 2 + 1)