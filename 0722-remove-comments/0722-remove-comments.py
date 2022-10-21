class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        
        commented = False
        temp = ""
        
        for line in source:
            
            i = 0
            while i < len(line):
                if not commented:
                    if i == len(line) - 1:
                        temp += line[i]
                    else:
                        string = line[i: i + 2]
                        if string == "/*":
                            commented = True
                            i += 1
                        elif string == "//":
                            break
                        else:
                            temp += line[i]
                else:
                    string = line[i: i + 2]
                    if string == "*/":
                        commented = False
                        i += 1
                i += 1
            if len(temp) > 0 and not commented:
                res.append(temp)
                temp = ""
        return res