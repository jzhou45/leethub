/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    let [l, r] =[0, s1.length - 1];
    
    s1 = s1.split("");
    s1.sort();
    s1 = s1.join("");
    
    while (r < s2.length){
        let temp = s2.slice(l, r + 1).split("");
        temp.sort();
        
        if (s1 === temp.join("")){
            return true;
        };
        
        l ++;
        r ++;
    }
    
    return false;
};