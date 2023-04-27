# @param {String[]} words
# @param {String} pattern
# @return {String[]}
def find_and_replace_pattern(words, pattern)
    ret_val = [];
    words.each { |word| ret_val << word if cipher(word, pattern)}
    ret_val
end

def cipher(word, key)
    word_hash = {}
    (0...word.length).each { |idx| word_hash[word[idx]] = idx }
    key_hash = {}
    (0...key.length).each { |idx| key_hash[key[idx]] = idx }
    word_str = ""
    word.each_char { |char| word_str += word_hash[char].to_s }
    key_str = ""
    key.each_char { |char| key_str += key_hash[char].to_s }
    return true if word_str == key_str
    return false
end