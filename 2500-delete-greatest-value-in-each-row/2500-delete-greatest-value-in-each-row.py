class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for subarr in grid:
            subarr.sort(reverse=True)
            
        res = 0
        
        for i in range(len(grid[0])):
            curr_max = 0
            for subarr in grid:
                curr_max = max(subarr[i], curr_max)
            res += curr_max
            
        return res