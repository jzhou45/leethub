class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            counter = 0
            for j in nums:
                if i != j:
                    if j < i:
                        counter += 1
            arr.append(counter)
        return arr  