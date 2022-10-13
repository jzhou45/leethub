class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        
        a, b, c = 0, 1, 2
        
        while c < len(nums):
            ab = nums[a] + nums[b] > nums[c]
            bc = nums[b] + nums[c] > nums[a]
            ca = nums[c] + nums[a] > nums[b]
            
            if ab and bc and ca:
                return nums[a] + nums[b] + nums[c]
            else:
                a += 1
                b += 1
                c += 1
                
        return 0