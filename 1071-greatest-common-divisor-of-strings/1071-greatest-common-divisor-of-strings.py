class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        for i in range(len(str2)):
            arr = str1.split(str2[:i + 1])
            arr2 = str2.split(str1[:i + 1])
            if len("".join(arr)) == 0 and len("".join(arr2)) == 0 and (len(str2[:i + 1]) < len(str1) or len(str2[:i + 1]) == len(str1) == len(str2)):
                res = str2[:i + 1]
        return res