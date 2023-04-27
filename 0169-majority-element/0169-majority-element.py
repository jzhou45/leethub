class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        ret_val = max(dict, key = dict.get)
        return ret_val