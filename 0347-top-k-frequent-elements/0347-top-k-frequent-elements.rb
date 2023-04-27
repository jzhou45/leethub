# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def top_k_frequent(nums, k)
    count = Hash.new(0)
    freq = Array.new(nums.length + 1) { [] }
    
    nums.each { |num| count[num] = 1 + count.fetch(num, 0)}
    count.each { |n, c| freq[c] << n }
    
    res = []
    (freq.length - 1).downto(1) do |idx|
        freq[idx].each do |num|
            res << num
            return res if res.length == k
        end
    end
end