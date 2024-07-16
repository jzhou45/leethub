/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const res = {}
    
    for (const str of strs) {
        const sorted = str.split('').sort().join('')
        if (sorted in res) {
            res[sorted].push(str)
        } else {
            res[sorted] = [str]
        }
    }
    
    return Object.values(res)
};