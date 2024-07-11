/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let currMax = 0
    let [l, r] = [0, 1]
    
    while (r < prices.length) {
        if (prices[r] < prices[l]) {
            l = r
            r = l + 1
        } else {
            const currSum = prices[r] - prices[l]
            if (currSum > currMax) currMax = currSum
            r ++
        }
    }
    
    return currMax
};