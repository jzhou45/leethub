# @param {Integer[]} nums
# @return {Boolean}
def divide_array(nums)
    nums = nums.sort
    (0...nums.length).step(2) do |idx|
        if nums[idx] != nums[idx + 1]
            return false
        end
    end
    return true
end