class Solution:
    def pivotInteger(self, n: int) -> int:
        l, r  = 1, n
        l_sum, r_sum = 1, n
        
        while l < r:
            if l_sum < r_sum:
                l += 1
                l_sum += l
            else:
                r -= 1
                r_sum += r
        
        return l if l_sum == r_sum else -1