/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    let [take, noTake] = [cost[0], 0];
    
    for (let i = 1; i < cost.length; i++){
        let temp = take;
        take = Math.min(take, noTake) + cost[i];
        noTake = temp;
    }
    
    return Math.min(take, noTake);
};