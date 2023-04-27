# @param {Integer[]} nums
# @return {Integer}
def num_identical_pairs(nums)
    good = 0
    for i in (0...nums.length)
        for j in (0...nums.length)
            if nums[i] == nums [j] and i != j
                good = good + 1
            end
        end
    end
    good = good/2
    return good
end