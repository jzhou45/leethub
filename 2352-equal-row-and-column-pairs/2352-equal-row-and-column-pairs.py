class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        seen = {}
        
        for i in range(len(grid)):
            row = ""
            for num in grid[i]:
                row += str(num) + " "
            if row in seen:
                seen[row][0] += 1
            else:
                seen[row] = [1, 0]
        
            col = ""
            for j in range((len(grid))):
                col += str(grid[j][i]) + " "
            if col in seen:
                seen[col][1] += 1
            else:
                seen[col] = [0, 1]

        res = 0
        
        for r, c in seen.values():
            res += r * c

        return res