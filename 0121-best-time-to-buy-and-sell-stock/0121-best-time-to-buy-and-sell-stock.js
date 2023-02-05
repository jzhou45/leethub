/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxProfit = 0;
    let [left, right] = [0, 1];
    
    while (right < prices.length){
        if (prices[left] < prices[right]){
            maxProfit = Math.max(maxProfit, prices[right] - prices[left]);
        } else{
            left = right;
        }
        right ++;
    }
    
    return maxProfit;
};