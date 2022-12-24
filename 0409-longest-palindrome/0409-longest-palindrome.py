class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        count = list(counter.values())
        odd = 0
        currSum = 0
        for n in count:
            if n % 2 == 0:
                currSum += n
            else:
                odd = 1
                currSum += n - 1
        return odd + currSum