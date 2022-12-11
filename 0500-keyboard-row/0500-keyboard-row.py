class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set([*"qwertyuiopQWERTYUIOP"])
        second = set([*"asdfghjklASDFGHJKL"])
        third = set([*"zxcvbnmZXCVBNM"])
        
        res = []
        
        for word in words:
            search = 0
            
            if word[0] in first:
                search = 1
            elif word[0] in second:
                search = 2
            else:
                search = 3
        
            tf = True
            for char in word:
                if search == 1:
                    if char not in first:
                        tf = False
                        break
                elif search == 2:
                    if char not in second:
                        tf = False
                        break
                else:
                    if char not in third:
                        tf = False
                        break
            
            if tf:
                res.append(word)
                
        return res