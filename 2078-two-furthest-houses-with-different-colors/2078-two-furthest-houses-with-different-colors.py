class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ltor = 0
        for i in range(len(colors) - 1, 0, -1):
            if colors[i] != colors[0]:
                ltor = i
                break
        rtol = 0
        for j in range(len(colors)):
            if colors[j] != colors[len(colors) - 1]:
                rtol = len(colors) - 1 - j
                break
        return max(ltor, rtol)