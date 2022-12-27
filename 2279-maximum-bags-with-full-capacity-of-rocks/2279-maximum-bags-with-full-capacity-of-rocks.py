class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        new = []
        for i in range(len(capacity)):
            new.append(capacity[i] - rocks[i])
        new.sort()
        res = 0
        i = 0
        while additionalRocks > 0 and i < len(new):
            if new[i] == 0:
                res += 1
            elif additionalRocks - new[i] >= 0:
                additionalRocks -= new[i]
                res += 1
            i += 1
        return res