# @param {String} s
# @return {String}
def sort_sentence(s) #"is2 sentence4 This1 a3"
    wordArr = s.split(" ") #["is2", "sentence4", "This1", "a3"]
    arr = []
    wordArr.each do |word|
        key = word[-1]
        (0...(word.length - 1)).each do |charidx|
            key = key + word[charidx]
        end
        arr << key
    end #["2is", "4sentence", "1This", "3a"]
    sortedArr = arr.sort #["1This", "2is", "3a", "4sentence"]
    lastArr = []
    sortedArr.each do |word2|
        key2 = ""
        (1...(word2.length)).each do |charidx2|
            key2 = key2 + word2[charidx2]
        end
        lastArr << key2
    end
    final = lastArr.join(" ")
    return final
end