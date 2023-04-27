class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lst = list(str(n))
        product = 1
        sumlst = 0
        for i in lst:
            product = product * int(i)
            sumlst += int(i)
        return product - sumlst