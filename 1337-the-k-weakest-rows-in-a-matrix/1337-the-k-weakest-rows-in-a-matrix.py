class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        
        for i, row in enumerate(mat):
            count = Counter(row)
            heapq.heappush(heap, (count[1], i))
        
        res = []
        
        for j in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res