# @param {Integer} n
# @return {Integer[]}
def sum_zero(n)
    accum = 0
    ret_val = []
    if n.even?
        while accum < n
            (1..n/2).each do |ele|
                ret_val << ele
                ret_val << 0 - ele
                accum += 2
            end
        end
    end
    if n.odd?
        ret_val << 0
        n += -1
        while accum < n
            (1..n/2).each do |ele2|
                ret_val << ele2
                accum += 1
                ret_val << 0 - ele2
                accum += 1
            end
        end
    end
    ret_val 
end