class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_nums = {}
        max_num = 1
        for num in nums:
            all_nums[num] = True
            max_num = max(num, max_num)
        res = []
        max_num = max(len(nums), max_num)
        for i in range(1, max_num + 1):
            if i not in all_nums:
                res.append(i)
        return res