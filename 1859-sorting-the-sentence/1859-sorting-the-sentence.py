class Solution:
    def sortSentence(self, s: str) -> str:
        arr, temp = [], ""
        
        def placeWord():
            nonlocal arr, temp
            num = int(temp[-1])
            while len(arr) <= num:
                arr.append(None)
            arr[num] = temp[:-1]
            return
        
        for char in s:
            if char == " ":
                placeWord()
                temp = ""
            else:
                temp += char
        
        placeWord()
        return " ".join(arr[1:])