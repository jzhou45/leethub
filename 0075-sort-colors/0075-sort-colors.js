/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    const counter = {0:0, 1:0, 2:0}
    
    for (const num of nums) {
        counter[num]++
    }
    
    let i = 0
    while (counter[0] > 0) {
        nums[i] = 0
        i++
        counter[0]--
    }
    while (counter[1] > 0) {
        nums[i] = 1
        i++
        counter[1]--
    }
    while (counter[2] > 0) {
        nums[i] = 2
        i++
        counter[2]--
    }
};