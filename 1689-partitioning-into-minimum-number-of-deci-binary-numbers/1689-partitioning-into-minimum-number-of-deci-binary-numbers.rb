# @param {String} n
# @return {Integer}
def min_partitions(n)
    num = 0
    n.each_char do |char| 
        num = char.to_i if char.to_i > num 
        break if num == 9
    end
    num
end