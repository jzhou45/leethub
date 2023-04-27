# @param {Integer[]} piles
# @return {Integer}
def max_coins(piles)
    my_pile = 0
    arr = piles.sort
    while arr.length > 0
        arr.pop
        my_pile += arr[-1]
        arr.pop
        arr.shift
    end
    my_pile
end