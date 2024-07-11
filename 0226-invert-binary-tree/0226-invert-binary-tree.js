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
 * @return {TreeNode}
 */
var invertTree = function(root) {
    let node = root
    
    const dfs = (node) => {
        if (!node?.left && !node?.right) return
        
        const temp = node.right
        node.right = node.left
        node.left = temp
        
        dfs(node.right)
        dfs(node.left)
    }
    
    dfs(root)
    return root
};