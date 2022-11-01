class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        visited2 = set()
        
        def new_island(row, col):
            if (row, col) in visited:
                return
            if row >= len(grid1) or row < 0 or col >= len(grid1[0]) or col < 0:
                return
            if grid1[row][col] == 0:
                return
            
            visited.add((row, col))
            
            new_island(row + 1, col)
            new_island(row - 1, col)
            new_island(row, col + 1)
            new_island(row, col - 1)
            
            return
        
        def subisland(row, col):
            nonlocal in_island
            if (row, col) in visited2:
                return False
            if row >= len(grid2) or row < 0 or col >= len(grid2[0]) or col < 0:
                return False
            if grid2[row][col] == 0:
                return False
            if (row, col) not in visited:
                in_island = False
            
            visited2.add((row, col))
            
            subisland(row + 1, col)
            subisland(row - 1, col)
            subisland(row, col + 1)
            subisland(row, col - 1)
            
            return True
        
        res = 0
        
        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                new_island(row, col)
                in_island = True
                if subisland(row, col) and in_island:
                    res += 1
        
        return res