class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(1, numRows):
            temp = [0] + res[-1] + [0]
            arr = []
            for j in range(len(res[-1]) + 1):
                arr.append(temp[j] + temp[j + 1])
            res.append(arr)    
            
        return res