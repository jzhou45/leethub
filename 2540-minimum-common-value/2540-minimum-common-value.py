class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        x, y = 0, 0
        
        while x < len(nums1) and y < len(nums2):
            if nums1[x] == nums2[y]: return nums1[x]
            if nums1[x] > nums2[y]:
                y += 1
            else:
                x += 1
                
        return -1