class Solution:
    def originalDigits(self, s: str) -> str:
        chars = ["z", "w", "u", "x", "g", "h", "f", "s", "o", "i"]
        count = {chars[i]: 0 for i in range(len(chars))}
        
        for char in s:
            if char in count:
                count[char] += 1
                
        res = {str(j): "" for j in range(10)}
        
        for key, val in count.items():
            if key == "z":
                res["0"] += "0" * val
                count["o"] -= val
            elif key == "w":
                res["2"] += "2" * val
                count["o"] -= val
            elif key == "u":
                res["4"] += "4" * val
                count["o"] -= val
                count["f"] -= val
            elif key == "x":
                res["6"] += "6" * val
                count["i"] -= val
                count["s"] -= val
            elif key == "g":
                res["8"] += "8" * val
                count["h"] -= val
                count["i"] -= val
            elif key == "h":
                res["3"] += "3" * val
            elif key == "f":
                res["5"] += "5" * val
                count["i"] -= val
            elif key == "s":
                res["7"] += "7" * val
            elif key == "o":
                res["1"] += "1" * val
            else:
                res["9"] += "9" * val
                
        return "".join(list(res.values()))
                