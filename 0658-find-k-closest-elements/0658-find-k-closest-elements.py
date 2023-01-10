class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        
        for num in arr:
            heapq.heappush(heap, (abs(x-num), num))
        
        res = []
        
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return sorted(res)