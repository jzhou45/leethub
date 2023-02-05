/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const alphanum = new           Set("abcdefghijklmnopqrstuvwxyzABCDEFGHJIKLMNOPQRSTUVWXYZ0123456789".split(""));
    
    let i = 0;
    let j = s.length - 1;
    
    while (i < j){
        console.log(s[i], s[j])
        if (!alphanum.has(s[i])){
            i ++;
        } else if (!alphanum.has(s[j])){
            j --;
        } else if (s[i].toLowerCase() !== s[j].toLowerCase()){
            return false;
        } else{
            i ++;
            j --;
        }
    }
    
    return true;
};