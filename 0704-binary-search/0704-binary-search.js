/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    if (nums.length === 1 && target !== nums[0]){
        return -1;
    }
    let mid = Math.floor(nums.length / 2);
    let left = nums.slice(0, mid);
    let right = nums.slice(mid);

    if (nums[mid] === target){
        return mid;
    } else if (target < nums[mid]){
        let leftNum = search(left, target);
        if (leftNum === -1){
            return -1;
        }
        return leftNum;
    } else {
        search(right);
        let rightNum = search(right, target);
        if (rightNum === -1){
            return -1;
        }
        return mid + rightNum;
    }
};