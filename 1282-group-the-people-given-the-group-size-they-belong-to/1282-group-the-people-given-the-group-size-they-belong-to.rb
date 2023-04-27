# @param {Integer[]} group_sizes
# @return {Integer[][]}
def group_the_people(group_sizes)
    hash = {}

    group_sizes.each_with_index do |ele, idx|
        if hash.key?(ele)
            hash[ele] << idx
        else
            hash[ele] = [idx]
        end
    end
    ret_val = []
    hash.each do |k, v|
        v.each_slice(k) { |a| ret_val << a}
    end
    ret_val
end