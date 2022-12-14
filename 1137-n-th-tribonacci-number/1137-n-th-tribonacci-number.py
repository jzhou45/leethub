class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]
        
        while len(arr) <= n:
            arr.append(sum(arr[-3:]))
        
        return arr[n]