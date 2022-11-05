class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums1):
            searched = False
            for num2 in nums2:
                if not searched and num2 == num:
                    searched = True
                elif searched and num2 > num:
                    res.append(num2)
                    break
            if len(res) != i + 1:
                res.append(-1)
        return res
                    