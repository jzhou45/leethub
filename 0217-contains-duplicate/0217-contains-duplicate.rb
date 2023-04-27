# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
    hash = Hash.new(0)
    nums.each do |num|
        hash[num] += 1
        return true if hash[num] == 2
    end
    false
end