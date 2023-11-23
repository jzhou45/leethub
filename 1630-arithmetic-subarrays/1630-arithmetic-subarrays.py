class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            subarr = nums[l[i]:r[i] + 1]
            subarr.sort()
            diff = subarr[1] - subarr[0]
            arth = True
            for j in range(len(subarr) -1, 1, -1):
                if subarr[j] - subarr[j - 1] != diff: 
                    arth = False
                    break
            res.append(arth)
        return res