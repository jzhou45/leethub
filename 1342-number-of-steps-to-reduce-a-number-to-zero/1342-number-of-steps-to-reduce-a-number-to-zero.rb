# @param {Integer} num
# @return {Integer}
def number_of_steps(num)
    counter = 0
    while num > 0
        if num.even?
            num = num / 2
            counter += 1
        else
            num = num - 1
            counter += 1
        end
    end
    counter
end