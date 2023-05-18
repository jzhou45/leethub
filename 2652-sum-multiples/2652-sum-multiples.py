class Solution:
    def sumOfMultiples(self, n: int) -> int:
        res = self.helper(n, 3).union(self.helper(n, 5).union(self.helper(n, 7)))
        return sum(list(res))
    
    def helper(self, n, m):
        res = set()
        for i in range(m, n + 1, m):
            res.add(i)
        return res