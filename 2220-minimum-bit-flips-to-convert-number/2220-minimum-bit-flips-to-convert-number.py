class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start).split("b")[1]
        goal = bin(goal).split("b")[1]
        
        res = 0
        
        while len(start) < len(goal):
            start = "0" + start
            
        while len(goal) < len(start):
            goal = "0" + goal
        
        for i in range(max(len(start), len(goal)) - 1, -1, -1):
            if start[i] != goal[i]:
                res += 1
        
        return res