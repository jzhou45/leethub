# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
    counter = 0
    (0...nums.length - 1).each do |idx|
        if nums[idx + 1] <= nums[idx]
            counter += nums[idx] + 1 - nums[idx + 1]
            nums[idx + 1] = nums[idx] + 1
        end
    end
    counter 
end