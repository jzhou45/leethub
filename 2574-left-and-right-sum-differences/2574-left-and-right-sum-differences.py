class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0 for i in range(len(nums) + 1)]
        rightSum = [0 for i in range(len(nums) + 1)]
        
        for i in range(len(nums)):
            leftSum[i + 1] += nums[i] + leftSum[i]
            
        leftSum.pop()
        
        for j in range(len(nums) - 1, -1, -1):
            rightSum[j - 1] += nums[j] + rightSum[j]
            
        rightSum.pop()
        
        res = []
        
        for k in range(len(leftSum)):
            res.append(abs(leftSum[k] - rightSum[k]))
            
        return res