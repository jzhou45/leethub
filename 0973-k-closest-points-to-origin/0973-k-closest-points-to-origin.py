class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        
        for point in points:
            x, y = point
            heapq.heappush(dist, (math.sqrt((0 - x)**2 + (0 - y)**2), [x, y]))
        
        res = []
        
        for i in range(k):
            res.append(heapq.heappop(dist)[1])
        
        return res