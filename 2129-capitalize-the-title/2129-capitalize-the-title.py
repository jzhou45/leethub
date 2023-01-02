class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")
        res = []
        
        for word in words:
            if len(word) > 2:
                res.append(word.capitalize())
            else:
                res.append(word.lower())
        
        return " ".join(res)