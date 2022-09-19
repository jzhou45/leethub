class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i, word in enumerate(strs):
            sortedword = "".join(sorted(word))
            if sortedword in anagrams:
                anagrams[sortedword].append(i)
            else:
                anagrams[sortedword] = [i]
        ret_val = []
        for value in anagrams.values():
            temp = []
            for j in value:
                temp.append(strs[j])
            ret_val.append(temp)
        return ret_val