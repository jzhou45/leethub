class Solution:
    def canJump(self, arr: List[int]) -> bool:
        r, traveled = 0, 0
        
        while r <= traveled:
            if traveled >= len(arr) - 1:
                return True
            traveled = max(traveled, r + arr[r])
            r += 1
        
        return False