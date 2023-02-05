/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let result = [];
    for (let i = 1; i <= n; i++){
        let [threeMod, fiveMod] = [i % 3 === 0, i % 5 === 0];
        if (threeMod && fiveMod){
            result.push("FizzBuzz");
        } else if (threeMod){
            result.push("Fizz");
        } else if (fiveMod){
            result.push("Buzz");
        } else{
            result.push(i.toString( ));
        }
    }
    
    return result;
};