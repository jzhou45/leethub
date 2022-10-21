class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = {}
        
        for i, num in enumerate(nums):
            if num in count:
                count[num].append(i)
            else:
                count[num] = [i]
                
        vals = []
        
        for val in list(count.values()):
            if len(val) > 1:
                vals.append(val)
        
        for arr in vals:
            for i, num in enumerate(arr):
                for j in range(i + 1, len(arr)):
                    if nums[num] == nums[arr[j]] and abs(num -arr[j]) <= k:
                        return True
        
        return False