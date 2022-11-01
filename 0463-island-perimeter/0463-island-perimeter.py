class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def check(row, col):
            res = 0
            if row - 1 >= 0 and grid[row-1][col] == 1:
                res += 1
            if row + 1 < len(grid) and grid[row+1][col] == 1:
                res += 1
            if col - 1 >= 0 and grid[row][col-1] == 1:
                res += 1
            if col + 1 < len(grid[0]) and grid[row][col+1] == 1:
                res += 1
            return res
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    sides = check(i, j)
                    res += 4 - sides
        return res
                