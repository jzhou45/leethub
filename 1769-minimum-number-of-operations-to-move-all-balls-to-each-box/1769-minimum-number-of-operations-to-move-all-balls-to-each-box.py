class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ball_locations = []
        for i, num in enumerate(boxes):
            if num == "1":
                ball_locations.append(i)
        res = []
        ball_len = len(ball_locations)
        
        for j in range(len(boxes)):
            curr_sum = 0
            for ball_loc in ball_locations:
                curr_sum += abs(j - ball_loc)
            res.append(curr_sum)
        
        return res