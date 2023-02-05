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
        
        return "/" + "/".join(stack)