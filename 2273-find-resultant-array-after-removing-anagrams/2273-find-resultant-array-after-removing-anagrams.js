/**
 * @param {string[]} words
 * @return {string[]}
 */
var removeAnagrams = function(words) {
    const res = []
    
    const sortString = (str) => str.split('').sort().join('')
    
    let previous = [sortString(words[0]), words[0]]
    let i = 1
    
    while (i < words.length) {
        const sorted = sortString(words[i])
        
        if (sorted !== previous[0]) {
            res.push(previous[1])
            previous = [sorted, words[i]]
        }
        
        i++
    }
    
    res.push(previous[1])
    
    return res
};