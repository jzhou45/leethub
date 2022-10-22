class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        knight_moves = [[1,2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
        memo = {}
        
        def dp(cur_k, cur_r, cur_c):
            if (cur_k, cur_r, cur_c) in memo: return memo[(cur_k, cur_r, cur_c)]
        
            if cur_k == k:
                return 1
            
            prob = 0
            
            for i in knight_moves:
                new_r = cur_r + i[0]
                new_c = cur_c + i[1]
                
                if 0 <= new_r < n and 0 <= new_c < n:
                    prob += (1 / 8 * dp(cur_k + 1, new_r, new_c))
                    
            memo[(cur_k, cur_r, cur_c)] = prob
            
            return prob
            
        return dp(0, row, column)