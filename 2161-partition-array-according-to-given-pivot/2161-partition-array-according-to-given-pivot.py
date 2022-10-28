class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, mid, right = [], [], []
        for i in nums:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                mid.append(i)
        return left + mid + right