/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    path = path.split("/");
    let arr = [];
    
    for (let str of path){
        if (str.length < 1 || str == "."){
            continue;
        } else if (str == ".."){
            if (arr){
                arr.pop();
            }
        } else{
            arr.push(str);
        }
    }
    
    return `/${arr.join("/")}`;
};