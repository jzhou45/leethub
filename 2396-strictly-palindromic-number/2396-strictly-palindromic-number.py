import numpy as np

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            temp = np.base_repr(n, base=i)
            comp = temp
            temp = [*temp]
            temp.reverse()
            temp = "".join(temp)
            if comp != temp:
                return False
        return True