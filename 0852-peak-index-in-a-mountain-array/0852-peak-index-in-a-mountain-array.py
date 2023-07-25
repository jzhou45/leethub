class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) == 1: return 0
        mid = len(arr) // 2
        
        if len(arr) < 3:
            return 0 if arr[0] > arr[1] else 1
        elif arr[mid - 1] > arr[mid]:
            return self.peakIndexInMountainArray(arr[:mid])
        else:
            return mid + self.peakIndexInMountainArray(arr[mid:])