class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                if profit > maxProfit:
                    maxProfit = profit
            else:
                left = right
            right += 1
        return maxProfit