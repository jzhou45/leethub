class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        names_to_height = {}
        for i in range(len(names)):
            names_to_height[i] = heights[i]
        names_to_height = sorted(names_to_height.items(), key=lambda x:x[1], reverse=True)
        res = []
        for key, val in names_to_height:
            res.append(names[key])
        return res