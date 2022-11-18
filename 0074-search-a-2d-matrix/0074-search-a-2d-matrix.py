class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        
        while top <= bot:
            mid = (top + bot) // 2
            
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        
        if top > bot: return False
        
        l, r = 0, len(matrix[0]) - 1
        
        mid = (top + bot) // 2
        
        while l <= r:
            med = (l + r) // 2
            
            if target == matrix[mid][med]:
                return True
            elif target < matrix[mid][med]:
                r = med - 1
            else:
                l = med + 1
        
        return False