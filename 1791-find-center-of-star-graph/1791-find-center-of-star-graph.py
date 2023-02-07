class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = {}
        
        for subarr in edges:
            for num in subarr:
                count[num] = count.get(num, 0) + 1
                if count[num] == len(edges):
                    return num