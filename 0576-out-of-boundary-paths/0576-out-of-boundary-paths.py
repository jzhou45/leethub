class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        poss_moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        def dp(moves, curr_row, curr_col):
            if (moves, curr_row, curr_col) in memo: return memo[(moves, curr_row, curr_col)]
            
            if moves == maxMove: return 0
            
            res = 0
            
            for i in poss_moves:
                new_row = curr_row + i[0]
                new_col = curr_col + i[1]
                
                if 0 <= new_row < m and 0 <= new_col < n:
                    res += dp(moves + 1, new_row, new_col)
                else:
                    res += 1
            
            memo[(moves, curr_row, curr_col)] = res
            
            return res
        
        return dp(0, startRow, startColumn) % (10**9 + 7)