class Solution:
    def romanToInt(self, s: str) -> int:
        stack = []
        trans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        for char in s:
            if stack:
                last = stack[-1]
                if last == 1 and (char == "V" or char == "X"):
                    stack.append(trans[char] - stack.pop())
                elif last == 10 and (char == "L" or char == "C"):
                    stack.append(trans[char] - stack.pop())
                elif last == 100 and (char == "D" or char == "M"):
                    stack.append(trans[char] - stack.pop())
                else:
                    stack.append(trans[char])
            else:
                stack.append(trans[char])
        
        return sum(stack)