class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        sorted_heights = sorted(heights)
        
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                res += 1
        
        return res