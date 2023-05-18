class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        original = image[sr][sc]
        
        def travel(x, y):
            if (x, y) in visited: return
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]): return
            if image[x][y] != original:return
            
            visited.add((x, y))
            image[x][y] = color
            
            travel(x + 1, y)
            travel(x - 1, y)
            travel(x, y + 1)
            travel(x, y - 1)
        
        travel(sr, sc)
        return image