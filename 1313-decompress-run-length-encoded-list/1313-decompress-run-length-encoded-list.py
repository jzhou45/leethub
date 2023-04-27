class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        keys = []
        values = []
        for i in range(len(nums)):
            if i % 2:
                keys.append(nums[i])
            else: 
                values.append(nums[i])
        ret_val = []
        for j in range(len(values)):
            accum = 0
            while accum < values[j]:
                ret_val.append(keys[j])
                accum += 1
        return ret_val