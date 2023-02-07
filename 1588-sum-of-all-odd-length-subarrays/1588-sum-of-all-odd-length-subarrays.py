class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = 1
        res = 0
        
        while n <= len(arr):
            for i in range(len(arr) - n + 1):
                res += sum(arr[i:i+n])
            n += 2
            
        return res