class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        arr = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    arr[i][j] += 1 + arr[i + 1][j + 1]
                else:
                    arr[i][j] = max(arr[i + 1][j], arr[i][j + 1])
        
        return arr[0][0]
                    