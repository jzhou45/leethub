# @param {String[]} words
# @param {String} pref
# @return {Integer}
def prefix_count(words, pref)
    counter = 0
    words.each do |ele|
        if ele.include?(pref)
            arr = ele.split(pref)
            p arr
            if arr[0] == ""
                counter += 1
            end
            if arr == []
                counter += 1
            end
        end
    end
    counter
end