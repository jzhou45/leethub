class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        
        res = 0
        
        def new_island(row, col):
            if (row, col) in visited:
                return False
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return False
            if grid[row][col] == "0":
                return False
            
            visited.add((row, col))
            
            new_island(row, col + 1)
            new_island(row, col - 1)
            new_island(row + 1, col)
            new_island(row - 1, col)
            
            return True
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if new_island(row, col):
                    res += 1
        
        return res