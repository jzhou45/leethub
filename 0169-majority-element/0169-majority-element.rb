# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
    hash = Hash.new(0)
    nums.each do |num|
        hash[num] += 1
    end
    max_kv = hash.max_by { |k,v| v}
    max_kv[0]
end