# @param {Integer[]} arr
# @return {Integer[]}
def replace_elements(arr)
    max_right = -1
    (arr.length - 1).downto(0).each do |idx|
        new_max = [max_right, arr[idx]].max
        arr[idx] = max_right
        max_right = new_max
    end
    arr
end