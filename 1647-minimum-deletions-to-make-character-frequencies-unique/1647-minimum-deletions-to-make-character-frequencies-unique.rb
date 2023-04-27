# @param {String} s
# @return {Integer}
def min_deletions(s)
    output = 0
    return output if s.length <= 1
    hash = Hash.new { |h, k| h[k] = [] }
    s.each_char.with_index { |char, idx| hash[char] << idx }
    arr = []
    hash.values.each { |subarr| arr << subarr.length }
    until arr == arr.uniq
        (1...arr.length).each do |idx|
            if arr[idx] == 0
                arr.delete_at(idx)
                break
            end
            if arr[0...idx].include?(arr[idx])
                arr[idx] -= 1
                output += 1
                break
            end
        end
    end
    output
end