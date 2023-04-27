class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ret_val = 0
        counter = 0
        first = s[0]
        for char in s:
            if char == first:
                counter += 1
            else:
                counter += -1
            if counter == 0:
                ret_val += 1
        return ret_val