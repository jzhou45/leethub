class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        x = []
        for i in accounts:
            x.append(sum(i))
        return max(x)