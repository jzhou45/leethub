# @param {Integer[]} nums
# @return {Integer}
def min_moves2(nums)
    count = 0
    nums.sort!
    median = nums[nums.length / 2]
    nums.each { |num| count += (median - num).abs }
    count
end