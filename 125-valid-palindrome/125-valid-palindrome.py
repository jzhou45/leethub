class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = string.ascii_lowercase
        nums = ([str(i) for i in range(0, 10)])
        first = 0
        last = len(s)-1
        while first < last:
            if s[first].lower() not in alphabet and s[first] not in nums:
                first += 1
                continue
            if s[last].lower() not in alphabet and s[last] not in nums:
                last -= 1
                continue
            if s[first].lower() == s[last].lower():
                first += 1
                last -= 1
            else:
                return False
        return True
