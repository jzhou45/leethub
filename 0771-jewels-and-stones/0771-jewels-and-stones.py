class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = {}
        
        for jewel in jewels:
            count[jewel] = 0
        
        for stone in stones:
            if stone in count:
                count[stone] += 1
        
        return sum(count.values())