class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [1]
        count = 0
        while count != rowIndex:
            temp = [0] + pascal + [0]
            new = []
            for i in range(len(pascal) + 1):
                new.append(temp[i] + temp[i + 1])
                pascal = new
            count += 1
        return pascal