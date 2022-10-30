class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        dummy = [*x]
        dummy.reverse()
        return x == "".join(dummy)