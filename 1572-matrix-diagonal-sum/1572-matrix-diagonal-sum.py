class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        
        for i in range(len(mat)):
            # print(mat[i][i])
            
            res += mat[i][i]
            if i != len(mat) - 1 - i:
                # print(mat[-1 - i][-1 - i])
                res += mat[i][-1 - i]
        
        return res
    
#     7 5
#     4 6
#     6 4
#     5 7
    
    
    
#     7319
#     3469
#     6966
#     9585