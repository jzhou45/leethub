class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = [0,0]
        heapq.heapify(largest)
        
        for num in nums:
            if num > largest[0]:
                heapq.heappop(largest)
                heapq.heappush(largest, num)
                
        return (largest[0] - 1) * (largest[1] - 1)