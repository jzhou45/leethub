class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        y=[]
        for i in sentences:
            x=1
            for j in i:
                if j==" ":
                    x = x+1
            y.append(x)
        return max(y)