import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse= [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = string.ascii_lowercase
        
        alpha_to_morse = {}
        for i in range(len(alphabet)):
            alpha_to_morse[alphabet[i]] = morse[i]
        
        res = set()
        
        for word in words:
            temp = ""
            for char in word:
                temp += alpha_to_morse[char]
            res.add(temp)
        
        return len(res)