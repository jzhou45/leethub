/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hash = {};
    
    for (let i = 0; i < nums.length; i++){
        if (target - nums[i] in hash){
            return [i, hash[target - nums[i]]];
        } else{
            hash[nums[i]] = i;
        }
    }
};