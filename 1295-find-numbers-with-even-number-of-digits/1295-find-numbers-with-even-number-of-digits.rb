# @param {Integer[]} nums
# @return {Integer}
def find_numbers(nums)
    ret_val = 0
    nums.each do |num|
        str = num.to_s
        counter = 0
        str.each_char do |char|
            counter += 1
        end
        if counter.even?
            ret_val += 1
        end
    end
    ret_val
end