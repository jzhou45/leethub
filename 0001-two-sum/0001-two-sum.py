class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dic:
                return [i, dic[diff]]
            dic[num] = i
                