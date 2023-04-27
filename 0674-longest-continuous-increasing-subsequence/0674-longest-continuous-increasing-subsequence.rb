# @param {Integer[]} nums
# @return {Integer}
def find_length_of_lcis(nums)
    arr = []
    accum = 1
    (0...nums.length - 1).each do |idx|
        if nums[idx] < nums[idx + 1]
            accum += 1
        else
            accum = 1
        end
        arr << accum
    end
    arr << accum
    arr.max 
end