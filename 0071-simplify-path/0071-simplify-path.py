class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/");
        
        stack = []
        
        for string in path:
            if stack and string == "..":
                stack.pop()
            elif not (len(string) < 1 or string == "." or string == ".."):
                stack.append(string)
        
        return "/%s"%('/'.join(stack))