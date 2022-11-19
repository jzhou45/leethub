class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] < 0 and nums[-1] > 0:
            l, r = 0, len(nums) - 1
            m = (l + r) // 2

            while l <= r:
                if nums[m] < 0:
                    l = m + 1
                else:
                    r = m - 1
                m = (l + r) // 2
                
            # m += 1
            
            res = []
            
            l, r = m, m + 1
        
            while l >= 0 and r < len(nums):
                if abs(nums[l]) < nums[r]:
                    res.append(nums[l]**2)
                    l -= 1
                else:
                    res.append(nums[r]**2)
                    r += 1
            
            while l >= 0:
                res.append(nums[l]**2)
                l -= 1
                
            while r < len(nums):
                res.append(nums[r]**2)
                r += 1

            return res
        
        elif nums[0] >= 0:
            for i, num in enumerate(nums):
                nums[i] = num**2

            return nums
        else:
            res = []
            for i in range(len(nums) - 1, -1, -1):
                res.append(nums[i] ** 2)

            return res