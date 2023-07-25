class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        mid = len(arr) // 2
        print(arr)
        
        if len(arr) <= 3:
            return arr.index(max(arr))
        elif arr[mid - 1] > arr[mid]:
            return self.peakIndexInMountainArray(arr[:mid])
        else:
            return mid + self.peakIndexInMountainArray(arr[mid:])