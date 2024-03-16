class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        count = 0
        dic = {0: -1}
        
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
                
            if count in dic:
                res = max(i - dic[count], res)
            else:
                dic[count] = i

        
        return res