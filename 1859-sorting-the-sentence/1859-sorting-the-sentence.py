class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(' ')
        arr = [None] * (len(s) + 1)
        
        for word in s:
            new_word, num = word[:-1], int(word[-1])
            arr[num] = new_word
        
        return " ".join(arr[1:])
