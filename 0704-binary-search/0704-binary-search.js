/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    if (nums.length <= 1 && nums?.[0] !== target) return -1
    
    const mid = Math.floor((nums.length - 1) / 2)
    if (nums[mid] === target) return mid
    
    if (target < nums[mid]) {
        return search(nums.slice(0, mid), target)
    } else {
        const right = search(nums.slice(mid + 1), target)
        return (right === -1) ? -1 : right + mid + 1
    }
};