/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    let count = {};
    
    for (let jewel of jewels){
        count[jewel] = 0
    }
    
    for (let stone of stones){
        if (stone in count){
            count[stone] ++;
        }
    }
    
    return Object.values(count).reduce((currSum, num) => currSum + num, 0);
};