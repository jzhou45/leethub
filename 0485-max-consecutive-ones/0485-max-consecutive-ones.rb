# @param {Integer[]} nums
# @return {Integer}
def find_max_consecutive_ones(nums)
    arr = []
    accum = 0
    nums.each_with_index do |ele|
        if ele == 1
            accum += 1
        else
            accum = 0
        end
        arr << accum
    end
    p arr
    arr.max
end