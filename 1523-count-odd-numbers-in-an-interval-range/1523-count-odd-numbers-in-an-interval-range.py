class Solution:
    def countOdds(self, low: int, high: int) -> int:
        high_odd = high % 2 != 0
        low_odd = low % 2 != 0
        
        if not high_odd and not low_odd:
            return (high - low) // 2
        
        return (high - low) // 2 + 1