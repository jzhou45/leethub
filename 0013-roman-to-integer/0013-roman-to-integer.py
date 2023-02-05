class Solution:
    def romanToInt(self, s: str) -> int:
        trans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        stack = [trans[s[0]]]
        
        for char in s[1:]:
            last = stack[-1]
            if stack and ((last == 1 and (char == "V" or char == "X")) or (last == 10 and (char == "L" or char == "C")) or (last == 100 and (char == "D" or char == "M"))):
                stack.append(trans[char] - stack.pop())
            else:
                stack.append(trans[char])
        
        return sum(stack)