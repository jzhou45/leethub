# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def top_k_frequent(nums, k)
    hash = Hash.new(0)
    nums.each { |num| hash[num] += 1 }
    arr = []
    until hash.values.empty?
        max = hash.max_by { |k, v| v }
        arr << max[0]
        hash.delete(max[0])
    end
    ret_val = []
    k.times { ret_val << arr.shift }
    ret_val
end