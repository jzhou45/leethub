class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        
        res = 0
        
        def dfs(row, col):
            if (row, col) in visited:
                return 0
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return 0
            if grid[row][col] == 0:
                return 0
            
            visited.add((row, col))
            
            area = 1
            area += dfs(row + 1, col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)
            
            return area
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                res = max(res, dfs(row, col))
        
        return res