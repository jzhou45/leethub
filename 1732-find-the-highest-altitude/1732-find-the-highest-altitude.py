class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_sum = curr_max = 0
        
        for num in gain:
            curr_sum += num
            curr_max = max(curr_max, curr_sum)
        
        return curr_max