/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const counter = {}
    
    for (const char of s) (char in counter) ? counter[char]++ : counter[char] = 1
    
    for (const char of t) {
        if (!(char in counter)) return false
        counter[char]--
    }
    
    return Object.values(counter).every((count) => count === 0)
};