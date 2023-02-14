class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_arr = [-1 for _ in range(len(arr) + 1)]
        
        for i in range(len(arr) - 1, 0, -1):
            max_arr[i] = max(arr[i], max_arr[i + 1])
        
        return max_arr[1:]