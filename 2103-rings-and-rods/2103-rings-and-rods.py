class Solution:
    def countPoints(self, rings: str) -> int:
        res = {"0": {"R":0, "G": 0, "B": 0},
              "1": {"R":0, "G": 0, "B": 0},
               "2": {"R":0, "G": 0, "B": 0},
               "3": {"R":0, "G": 0, "B": 0},
               "4": {"R":0, "G": 0, "B": 0},
               "5": {"R":0, "G": 0, "B": 0},
               "6": {"R":0, "G": 0, "B": 0},
               "7": {"R":0, "G": 0, "B": 0},
               "8": {"R":0, "G": 0, "B": 0},
               "9": {"R":0, "G": 0, "B": 0}
              }
        a, b = 0, 1
        while b < len(rings):
            res[rings[b]][rings[a]] += 1
            a += 2
            b += 2
        ans = 0
        for i in list(res.values()):
            add = True
            for j in list(i.values()):
                if j == 0:
                    add = False
                    break
            if add:
                ans += 1
        return ans
            
            
            