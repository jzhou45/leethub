# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        
        def dfs(node, count):
            nonlocal res
            if not node:
                return
            
            if (not node.left and not node.right):
                res = min(res, count)
                
            dfs(node.left, count + 1)
            dfs(node.right, count + 1)
            
        dfs(root, 1)
        
        return res if res != float("inf") else 0