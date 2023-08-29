/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // for (const i in nums) {
    //     const num = Number(i)
    //     let matchingIndex = nums.slice(num + 1).indexOf(target - nums[num])
    //     if (matchingIndex === -1) {
    //         matchingIndex = null
    //     } else {
    //         matchingIndex += (num + 1)
    //     }
    //     console.log(matchingIndex)
    //     if (matchingIndex) {
    //         return [num, matchingIndex]
    //     }
    // }
    const map = {};
    
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const diff = target - num;
        
        if (diff in map){
            return [map[diff], i];
        } else {
            map[num] = i;
        }
    }
};