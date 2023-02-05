/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function(root) {
    var res = Infinity;
    
    const dfs = (node, count) => {
        if (!node){
            return;   
        }
        
        if (!node.left && !node.right){
            res = Math.min(res, count);
        }
        
        dfs(node.left, count + 1);
        dfs(node.right, count + 1);
    }
    
    dfs(root, 1);
    
    return (res === Infinity) ? 0 : res;
};