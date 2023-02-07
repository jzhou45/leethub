class Solution:
    def countDigits(self, num: int) -> int:
        str_num = str(num)
        
        if len(str_num) == 1:
            return 1
        
        count = 0
        
        for char in str_num:
            if num % int(char) == 0:
                count += 1
                
        return count