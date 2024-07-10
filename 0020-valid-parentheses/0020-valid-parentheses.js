/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const chars = {'{': '}', '(': ')', '[': ']'}
    const stack = []
    
    for (const char of s) {
        // if not key then we need to either pop or return false
        if (char in chars) {
            stack.push(char)
        } else {
            const last = stack.pop()
            if (char !== chars[last]) return false
        }
    }
    
    return stack.length === 0
};