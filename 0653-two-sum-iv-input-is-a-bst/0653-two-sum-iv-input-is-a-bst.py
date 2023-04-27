# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hash = {}

        queue = [root]

        while len(queue) != 0:
            node = queue.pop()
            target = k - node.val
            if target in hash:
                return True
            else:
                hash[node.val] = target
            
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return False