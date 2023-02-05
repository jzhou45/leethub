class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/");
        
        stack = []
        
        for string in path:
            if len(string) < 1 or string == ".":
                continue
            elif string == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(string)
        
        res = ""
        
        for string2 in stack:
            res += "/" + string2
        
        return res if len(res) > 0 else "/"