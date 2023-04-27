class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for char in operations:
            if char == "+":
                score.append(score[-1] + score[-2])
            elif char == "C":
                score.pop()
            elif char == "D":
                score.append(score[-1] * 2)
            else:
                score.append(int(char))
        return sum(score)