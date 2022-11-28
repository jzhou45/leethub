class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while n not in visited:
            visited.add(n)
            n = str(n)
            new = []
            for char in n:
                new.append(int(char)**2)
            n = sum(new)
            if n == 1: return True
            
        return False