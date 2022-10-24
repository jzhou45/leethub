class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        
        def rob1(nums):
            rob1, rob2 = 0, 0
            for money in nums:
                temp = max(money + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(rob1(nums[:-1]), rob1(nums[1:]))
            