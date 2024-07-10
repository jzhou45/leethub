/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const seen = {} // remainder: index
    
    for (const i in nums) {
        const num = nums[i]
        const remainder = target - num
        
        if (remainder in seen) return [seen[remainder], i]
        seen[num] = i
    }
};