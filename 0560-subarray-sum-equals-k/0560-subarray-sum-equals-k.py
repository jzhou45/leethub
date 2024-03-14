class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        curr_sum = res = 0
        
        for num in nums:
            curr_sum += num
            remain = curr_sum - k

            res += prefix.get(remain, 0)
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            
        return res