# @param {Integer[]} nums
# @return {Integer[]}
def smaller_numbers_than_current(nums)
    hash = Hash.new(-1)
    arr = nums.sort
    arr.each_with_index do |num, idx|
        hash[num] = idx if hash[num] == -1
    end
    ret_val = []
    nums.each { |num| ret_val << hash[num] }
    ret_val
end