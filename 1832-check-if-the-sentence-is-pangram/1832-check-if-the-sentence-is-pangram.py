class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        check = {}
        for char in sentence:
            check[char] = 1 + check.get(char, 0)
            
        return len(check.items()) == 26