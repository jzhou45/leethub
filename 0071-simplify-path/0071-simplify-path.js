/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    path = path.split("/");
    let arr = [];
    
    for (let str of path){
        if (str == ".."){
            arr.pop();
        } else if (!(str.length < 1 || str == ".")){
            arr.push(str);
        }
    }
    
    return `/${arr.join("/")}`;
};