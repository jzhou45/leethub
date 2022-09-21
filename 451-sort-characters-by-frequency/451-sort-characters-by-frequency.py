class Solution:

    def frequencySort(self, s: str) -> str:
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        res = ""
        for i in sorted_count:
            for j in range(i[1]):
                res += i[0]
        return res
            