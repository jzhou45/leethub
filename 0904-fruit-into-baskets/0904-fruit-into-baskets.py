class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        
        l, r, diff = 0, 0, 0
        
        tracking = set()
        while r < len(fruits):
            if len(tracking) == 0:
                tracking.add(fruits[r])
                r += 1
            elif len(tracking) == 1 and fruits[r] not in tracking:
                diff = r
                tracking.add(fruits[r])
                r += 1
            elif len(tracking) == 2 and fruits[r] not in tracking:
                res = max(res, r - l)
                tracking.remove(fruits[l])
                l = diff
                diff = r
                r = l + 1
            else:
                r += 1
        
        if len(tracking) <= 2:
            res = max(res, r - l)
        return res