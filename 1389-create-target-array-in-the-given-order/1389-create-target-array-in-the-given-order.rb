# @param {Integer[]} nums
# @param {Integer[]} index
# @return {Integer[]}
def create_target_array(nums, index)
    ret_val = []
    (0...nums.length).each do |idx|
        ret_val.insert(index[idx], nums[idx])
    end
    ret_val
end