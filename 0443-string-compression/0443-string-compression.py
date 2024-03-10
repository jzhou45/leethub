class Solution:
    def compress(self, chars: List[str]) -> int:
        c = chars[0]
        n = 0
        i = 0
        
        def addNums():
            nonlocal n, i, chars
            if n > 1:
                for num in str(n):
                    chars[i] = num
                    i += 1
        
        for char in chars:
            if char == c:
                n += 1
            else:
                chars[i] = c
                i += 1
                addNums()
                c = char
                n = 1

        chars[i] = c
        i += 1
        addNums()
        
        return i