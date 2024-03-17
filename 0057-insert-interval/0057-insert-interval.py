class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for subarr in intervals:
            if subarr[1] < newInterval[0]:
                res.append(subarr)
            elif subarr[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = subarr
            elif subarr[1] >= newInterval[0] or subarr[0] <= newInterval[1]:
                newInterval[0] = min(subarr[0], newInterval[0])
                newInterval[1] = max(subarr[1], newInterval[1])
                print
        res.append(newInterval)
        return res