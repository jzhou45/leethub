# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
    hash = Hash.new(0)
    nums.each do |num|
        hash[num] += 1
        hash.delete(num) if hash[num] == 2
    end
    hash.keys[0]
end