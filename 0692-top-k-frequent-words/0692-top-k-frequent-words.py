class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        for word in words:
            count[word] = 1 + count.get(word, 0)
            
        sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    
        
        res = []
        
        for i in range(0, k):
            res.append(sorted_count[i][0])
            
        return res