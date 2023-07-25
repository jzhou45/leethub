class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                return i - 1