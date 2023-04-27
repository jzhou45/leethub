# @param {Integer[]} nums
# @param {Integer[]} l
# @param {Integer[]} r
# @return {Boolean[]}
def check_arithmetic_subarrays(nums, l, r)
    arr = []
    (0...l.length).each do |idx|
        arr2 = []
        arr2 << l[idx]
        arr2 << r[idx]
        arr << arr2
    end #[[0, 2], [0, 3], [2, 5]]
    tfArr = []
    arr.each do |i|
        arr2 = nums[i[0]..i[1]] #[4, 6, 5][4, 6, 5, 9][5, 9, 3, 7]
        sortArr = arr2.sort #[4, 5, 6][4, 5, 6, 9][3, 5, 7, 9]
        diff = (sortArr[0] - sortArr[1]).abs
        tf = true
        (0...sortArr.length - 1).each do |j|
            if (sortArr[j] - sortArr[j+1]).abs != diff
                tf = false
            end
        end
        tfArr << tf
    end
    return tfArr
end