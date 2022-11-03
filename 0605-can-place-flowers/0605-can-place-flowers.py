class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) < 3:
            for num in flowerbed:
                if num == 1:
                    return False if n > 0 else True
            return True if n < 2 else False
        
        l, m, r = 0, 1, 2
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
            l += 1
            m = l + 1
            r = m + 1
        while r < len(flowerbed):
            if flowerbed[l] == 0 and flowerbed[m] == 0 and flowerbed[r] == 0:
                flowerbed[m] = 1
                n -= 1
                l = m + 1
                m = l + 1
                r = m + 1
            elif flowerbed[r] == 1:
                l = r + 1
                m = l + 1
                r = m + 1
            elif flowerbed[m] == 1:
                l = m + 1
                m = l + 1
                r = m + 1
            else:
                l += 1
                m += 1
                r += 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
        
        
        return n <= 0