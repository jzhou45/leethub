/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    let res = [];
    let temp = [];
    
    for (let i = 0; i < arr.length; i++) {
        temp.push(arr[i]);
        if ((i + 1) % size === 0) {
            res.push(temp);
            temp = [];
        }
    }
    
    if (temp.length) res.push(temp);
    return res;
};
