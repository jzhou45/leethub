/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let hash = {};
    
    for (let i of s){
        hash[i] = hash[i] + 1 || 1;
    }
    
    for (let j of t){
        if (j in hash){
            hash[j] --;
        } else{
            return false;
        }
    }
    
    for (let k of Object.values(hash)){
        if (k !== 0){
            return false;
        }
    }
    
    return true;
};