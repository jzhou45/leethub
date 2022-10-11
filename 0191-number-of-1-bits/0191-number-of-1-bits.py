class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n:
            n &= n - 1
            counter += 1
        return counter