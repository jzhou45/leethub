class Solution:
    def addDigits(self, num: int) -> int:
        num = [*str(num)]
        
        while len(num) > 1:
            new = 0
            
            for char in num:
                new += int(char)
            
            num = [*str(new)]
        
        return int(num[0])