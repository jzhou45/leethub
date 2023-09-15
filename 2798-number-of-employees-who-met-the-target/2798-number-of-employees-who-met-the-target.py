class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        num = 0
        for i in hours:
            if i >= target: num += 1
        
        return num