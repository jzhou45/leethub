class Solution:
    def countAsterisks(self, s: str) -> int:
        counting = True
        count = 0
        
        for char in s:
            if counting:
                if char == "|":
                    counting = False
                elif char == "*":
                    count += 1
            else:
                if char == "|":
                    counting = True
                    
        return count