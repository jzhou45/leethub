# @param {String} s
# @return {Integer}
def balanced_string_split(s)
    counter = 0
    ret_val = 0
    letter = s[0]
    s.each_char do |char|
        if char == letter
            counter += 1
        else
            counter += -1
        end
        if counter == 0
            ret_val += 1
        end
    end
    ret_val
end