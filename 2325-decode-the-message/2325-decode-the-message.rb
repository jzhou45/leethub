# @param {String} key
# @param {String} message
# @return {String}
def decode_message(key, message)
    alphabet = ('a'..'z').to_a
    hash = Hash.new(0)
    counter = 0
    key.each_char do |char|
        if hash[char] == 0 && char != " "
            hash[char] = alphabet[counter]
            counter += 1
        end
    end
    ret_val = ""
    message.each_char do |char2| 
        if char2 == " "
            ret_val += " "
        else
            ret_val += hash[char2]
        end
    end
    ret_val
end