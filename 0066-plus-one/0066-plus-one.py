class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits == [0]: return [1]
        
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                break
            digits[i] = 0
        
        if digits[0] == 0:
            return [1, 0] + digits[1:]
        else:
            return digits