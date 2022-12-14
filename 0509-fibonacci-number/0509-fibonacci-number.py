class Solution:
    def fib(self, n: int) -> int:
        arr = [0, 1]
        
        while len(arr) <= n:
            arr.append(sum(arr[-2:]))
        
        return arr[n]