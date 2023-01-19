class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        #count, [indices]
        hashmap = {}
        
        for i, num in enumerate(nums):
            if num in hashmap:
                count, arr = hashmap.get(num)
                hashmap[num] = (count + 1, arr + [i])
            else:
                hashmap[num] = (1, [i])
        
        curr_max = 0
        res = len(nums)
        
        for _, val in hashmap.items():
            count, arr = val
            if count > curr_max:
                curr_max = count
                res = arr[-1] - arr[0] + 1
            elif count == curr_max:
                cuur_max = count
                res = min(res, arr[-1] - arr[0] + 1)
        
        return res