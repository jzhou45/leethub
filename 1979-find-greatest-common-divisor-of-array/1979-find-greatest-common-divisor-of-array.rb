# @param {Integer[]} nums
# @return {Integer}
def find_gcd(nums)
    hash = {}
    (1..nums.min).each do |factors|
        if nums.min % factors == 0
            if hash.key?(factors)
                hash[factors] += 1
            else
                hash[factors] = 1
            end
        end
    end
    (1..nums.max).each do |factors2|
        if nums.max % factors2 == 0
            if hash.key?(factors2)
                hash[factors2] += 1
            else
                hash[factors2] = 1
            end
        end
    end
    arr = []
    hash.each do |ele| 
        if ele[1] == 2
            arr << ele[0]
        end
    end
    arr.max
end