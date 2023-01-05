class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        res = 0
        for num in list(count.values()):
            while num > 0:
                if num % 3 == 0:
                    res += num / 3
                    num = 0
                elif num % 2 == 0:
                    num -= 2
                    res += 1
                elif num < 2:
                    return -1
                elif num % 2 != 0:
                    num -= 3
                    res += 1
        return int(res)