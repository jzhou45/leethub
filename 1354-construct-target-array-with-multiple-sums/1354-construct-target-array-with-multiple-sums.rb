# @param {Integer[]} target
# @return {Boolean}
def is_possible(target)
    return false if target.length == 1 && target[0] != 1
    tf = false
    until tf
        idx = target.find_index(target.max)
        arr = target.dup
        arr.delete_at(idx)
        sum = arr.sum
        return true if arr.all? { |ele| ele == 1} && target[idx] > sum && target.sum.odd? && (target.length.odd? || target.length == 2)
        return false if sum > target[idx]
        if target[idx] > 2
            target[idx] = target[idx] % sum
        else
            target[idx] = target[idx] - sum
        end
        p target
        return true if target.all? { |ele| ele == 1 } 
        return false if target.any? { |ele| ele < 1 }
    end
end