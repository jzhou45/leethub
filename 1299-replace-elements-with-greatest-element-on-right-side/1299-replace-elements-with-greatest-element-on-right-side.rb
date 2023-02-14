# @param {Integer[]} arr
# @return {Integer[]}
def replace_elements(arr)
    ans = []
    (0...arr.length - 1).each do |idx|
         ans << arr.slice(idx + 1, arr.length).max
    end
    ans << - 1
    ans
end