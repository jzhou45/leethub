class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        curr_sum = 0
        prefix = {0: 0}
        
        for num in nums:
            curr_sum += num
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
        
        return prefix[0]