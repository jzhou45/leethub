class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        dic = {}
        for i in range(len(s)):
            dic[indices[i]] = s[i]
        keyz = dic.keys()
        keyz.sort()
        string = ""
        for j in keyz:
            string += dic[j]
        return string