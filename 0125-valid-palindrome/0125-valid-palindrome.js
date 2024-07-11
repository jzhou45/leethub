/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const alphanum = new Set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'.split(''))
    
    let [l, r] = [0, s.length - 1]
    
    const isSpace = (char) => char === ' '
    
    while (l < r) {
        if (!(alphanum.has(s[l]))) {
            l ++
        } else if (!(alphanum.has(s[r]))) {
            r --
        } else if (s[l].toLowerCase() !== s[r].toLowerCase()) {
            return false
        } else {
            l ++
            r --
        }
    }
    
    return true
};