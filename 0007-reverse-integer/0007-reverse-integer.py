class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        ans = 0
        
        if x[0] == "-":
            res = [*x]
            res.reverse()
            ans = 0 - int("".join(res[:len(x) - 1]))
        else:
            x = [*x]
            x.reverse()
            ans = int("".join(x))
            
        return ans if 0 - 2**31 <= ans <= 2**31 - 1 else 0