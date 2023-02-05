/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    };
    
    let stack = [];
    
    for (let i = 0; i < s.length; i++){
        let last = stack[stack.length - 1];
        let char = s[i];
        
        if (
            (last === 1 && (char === "V" || char === "X")) ||
            (last === 10 && (char === "L" || char === "C")) ||
            (last === 100 && (char === "D" || char === "M"))
        ){
            stack.push(dict[char] - stack.pop());
        } else{
            stack.push(dict[char]);
        }
    }
    
    return stack.reduce((currSum, num) => currSum + num, 0);
};