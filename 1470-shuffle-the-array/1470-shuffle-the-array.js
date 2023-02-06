/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    let res = [];
    let i = 0;
    
    while (n < nums.length){
        res.push(nums[i]);
        res.push(nums[n]);
        i++;
        n++;
    }
    
    return res;
};