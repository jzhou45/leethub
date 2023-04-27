class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        str_sum = 0
        int_sum = 0
        
        for num in nums:
            int_sum += num
            
            for char in str(num):
                str_sum += int(char)
        
        return abs(str_sum - int_sum)