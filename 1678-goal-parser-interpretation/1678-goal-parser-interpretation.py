class Solution:
    def interpret(self, command: str) -> str:
        string = command.replace("()", "o")
        string2 = string.replace("(al)", "al")
        return string2