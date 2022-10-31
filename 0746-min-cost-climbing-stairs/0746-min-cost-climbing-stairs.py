class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        no_take, take = 0, cost[0]
        i = 1
        while i < len(cost):
            dummy = take
            take = min(no_take, take) + cost[i]
            no_take = dummy
            i += 1
        return min(take, no_take)