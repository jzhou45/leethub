class Solution:
    def reverseWords(self, s: str) -> str:
        reverse = []
        split_s = s.split()
        for word in split_s:
            temp = ""
            for i in range(len(word) - 1, -1, -1):
                temp += word[i]
            reverse.append(temp)
        return " ".join(reverse)