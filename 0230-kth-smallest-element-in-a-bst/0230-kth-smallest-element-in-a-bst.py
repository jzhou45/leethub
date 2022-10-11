# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        all_nodes = []
        
        while len(stack) > 0:
            node = stack.pop()
            all_nodes.append(node.val)
            
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        
        all_nodes.sort()

        return all_nodes[k - 1]