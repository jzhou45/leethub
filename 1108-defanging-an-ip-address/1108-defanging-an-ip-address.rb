# @param {String} address
# @return {String}
def defang_i_paddr(address)
    split = address.split(".")
    join = split.join("[.]")
    return join
end