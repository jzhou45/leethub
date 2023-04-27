class Solution:
    def minDeletions(self, s: str) -> int:
        ret_val = 0
        if len(s) <= 1:
            return ret_val
        dict = {}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]].append(i)
            else:
                dict[s[i]] = [i]
        arr = []
        for j in dict.values():
            arr.append(len(j))
        while len(set(arr)) != len(arr):
            for k in range(1, len(arr)):
                if arr[k] == 0:
                    arr.pop(k)
                    break
                if arr[k] in arr[0:k]:
                    arr[k] += -1
                    ret_val += 1
                    break
        return ret_val