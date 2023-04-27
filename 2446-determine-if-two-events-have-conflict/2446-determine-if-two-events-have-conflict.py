class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1a = event1[0].split(":")
        event1b = event1[1].split(":")
        event2a = event2[0].split(":")
        event2b = event2[1].split(":")
        time1 = 100 * int(event1a[0]) + int(event1a[1])
        time2 = 100 * int(event1b[0]) + int(event1b[1])
        time3 = 100 * int(event2a[0]) + int(event2a[1])
        time4 = 100 * int(event2b[0]) + int(event2b[1])
        
        if time3 in range(time1, time2 + 1) or time1 in range(time3, time4 + 1):
            return True
        return False