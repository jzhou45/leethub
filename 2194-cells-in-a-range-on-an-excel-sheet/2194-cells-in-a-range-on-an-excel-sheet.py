class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start_let = s[0]
        start_num = s[1]
        end_let = s[3]
        end_num = s[4]
        
        res = []
        
        for char in range(ord(start_let), ord(end_let) + 1):
            for num in range(int(start_num), int(end_num) + 1):
                res.append(chr(char) + str(num))
            
        return res