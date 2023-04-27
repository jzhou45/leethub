# @param {Integer[]} nums
# @return {Boolean}
def check_possibility(nums)
    return true if nums == []
    ind = nil
    ind2 = nil
    (0...nums.length - 1).each do |idx|
        if nums[idx] > nums[idx + 1]
            ind = idx
            ind2 = idx + 1
            break
        end
    end
    clone = nums.dup
    clone.delete_at(ind) unless ind.nil?
    return true if clone == clone.sort
    clone2 = nums.dup
    clone2.delete_at(ind2) unless ind.nil?
    return true if clone2 == clone2.sort
    false
end