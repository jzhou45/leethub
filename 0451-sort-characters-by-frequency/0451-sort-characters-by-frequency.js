/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    let arr = [];
    for (let i = 0; i < 75; i++){
        arr.push([0, i]);
    }
    
    for (let j = 0; j < s.length; j++){
        arr[s.charCodeAt(j) - 48][0] ++;
    }
    
    arr.sort((a, b) => {
        if (a[0] > b[0]){
            return -1;
        } else if (a[0] < b[0]){
            return 1;
        } else{
            return 0
        }
    });
    
    let res = "";
    
    for (let subarr of arr){
        let [freq, char] = subarr;
        if (freq === 0){
            break;
        };
        res += String.fromCharCode(48 + char).repeat(freq);
    }
    
    return res;
};