class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        i = 0
        while i < len(str1) and i < len(str2):
            substring = str2[:i + 1]
            arr1 = str1.split(substring)
            arr2 = str2.split(substring)
            if len("".join(arr1)) == 0 and len("".join(arr2)) == 0:
                res = substring
            i += 1
        return res
            