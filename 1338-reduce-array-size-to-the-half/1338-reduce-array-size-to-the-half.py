class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        
        heap = []
        
        for _, val in count.items():
            heapq.heappush(heap, -val)
        
        size = len(arr)
        half = size / 2
        
        res = 0
        
        while size > half:
            size += heapq.heappop(heap)
            res += 1
        
        return res