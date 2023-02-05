/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    currPrefix = ""
    
    for (let i = 0; i < strs[0].length; i++){
        let temp = strs[0][i];
        let add = true;
        
        for (let j = 0; j < strs.length; j++){
            if (strs[j][i] !== temp){
                add = false;
                break;
            }
        }
        
        if (!add){
            break;
        } else{
            currPrefix += temp;
        }
    }
    
    return currPrefix;
};