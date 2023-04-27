# @param {Integer[][]} logs
# @return {Integer}
def maximum_population(logs)
    hash = Hash.new(0)
    logs.sort!
    logs.each do |subarr|
        (subarr[0]...subarr[1]).each do |ele|
            hash[ele] += 1
        end
    end
    ans = hash.max_by { |k, v| v }
    ans[0]
end