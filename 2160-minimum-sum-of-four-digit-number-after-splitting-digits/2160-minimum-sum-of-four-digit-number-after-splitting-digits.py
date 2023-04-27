class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        arr = list(num)
        new1 = []
        new2 = []
        for numString in arr:
            numString = int(numString)
        arr.sort()
        for i in range(len(arr)):
            if i % 2 != 0:
                new1.append(arr[i])
            else:
                new2.append(arr[i])
        xew1 = ''.join(new1)
        xew2 = ''.join(new2)
        sums = int(xew1) + int(xew2)
        return sums