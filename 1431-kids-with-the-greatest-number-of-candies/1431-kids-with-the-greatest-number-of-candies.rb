# @param {Integer[]} candies
# @param {Integer} extra_candies
# @return {Boolean[]}
def kids_with_candies(candies, extra_candies)
    max = candies.max
    arr = []
    candies.each do |num|
        if num + extra_candies >= max
            arr.push(true)
        else
            arr.push(false)
        end
    end
    return arr
end