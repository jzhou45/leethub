class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        arr = []
        idx1 = 0
        idx2 = len(nums) - 1
        for i in range(len(nums)/2):
            arr2 = []
            arr2.append(nums[idx1])
            arr2.append(nums[idx2])
            idx1 += 1
            idx2 += -1
            arr.append(arr2)
        arr3 = []
        for j in arr:
            arr3.append(sum(j))
        maxnum = max(arr3)
        return maxnum