# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res = True
        
        def travel(node1, node2):
            nonlocal res
            if node1.val != node2.val:
                res = False
                return

            if node1.left and node2.right:
                travel(node1.left, node2.right)
            elif node1.left or node2.right:
                res = False
                return

            if node1.right and node2.left:
                travel(node1.right, node2.left)
            elif node1.right or node2.left:
                res = False
                return
            
        if root.left and root.right:
            travel(root.left, root.right)
            return res
        elif root.left or root.right:
            return False
        else:
            return True