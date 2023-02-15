class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        str_num = ""
        for n in num:
            str_num += str(n)
        sums = int(str_num) + k
        
        str_num = str(sums)
        
        ans = []
        
        for char in str_num:
            ans.append(int(char))
            
        return ans