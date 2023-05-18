class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        string = ""
        for num in nums: string += str(num)
        return [int(i) for i in string]