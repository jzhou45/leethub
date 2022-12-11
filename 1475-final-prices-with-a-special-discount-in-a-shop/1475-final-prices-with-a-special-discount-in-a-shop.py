class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices)):
            temp = prices[i]
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    temp -= prices[j]
                    break
            res.append(temp)
        
        return res