/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

/*
loop through array
find the difference between the target and my value
save that into a hashmap, key = diff, value = index
check if the value is in the hashmap, if true, breakout
*/

var twoSum = function(nums, target) { //[2,7,11,15], 9
    const difference = {}; //7: 0
    let res = []; //0, 1
    
    for (let i = 0; i < nums.length; i++) { // 1
        const num = nums[i]; // 7
        const diff = target - num; // 9 - 7 = 2
        
        if (num in difference) {
            res = [difference[num], i];
            break;
        } else {
            difference[diff] = i;
        }
    }
    
    return res;
};