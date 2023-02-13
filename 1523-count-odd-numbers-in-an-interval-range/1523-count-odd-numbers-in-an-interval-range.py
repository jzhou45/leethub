class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # 5, 4, 3, 2, 1 = 3 odd high odd low
        # 5, 4, 3, 2 = 2 odd high even low 5 - 2 = 3 // 2 = 1
        # 6, 5, 4, 3, 2 = 2 even high even low 6 - 2 = 4 // 2 = 2
        # 6, 5, 4, 3 = 2 even high even low 6 - 3 = 3 // 2 = 1
        
        high_odd = high % 2 != 0
        low_odd = low % 2 != 0
        
        if not high_odd and not low_odd:
            return (high - low) // 2
        
#         if high_odd and low_odd:
#             return (high - low) // 2 + 1
        
#         if high_odd and not low_odd:
#             return (high - low) // 2 + 1
        
#         if not high_odd and low_odd:
        return (high - low) // 2 + 1