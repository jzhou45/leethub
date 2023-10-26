# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def travel(node):
            if node.left: travel(node.left)
            if node.right: travel(node.right)
            res.append(node.val)
            
        if root: travel(root)
        return res