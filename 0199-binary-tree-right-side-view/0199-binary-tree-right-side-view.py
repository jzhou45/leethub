from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right = []
        queue = deque([root])
        
        while queue:
            right_side = None
            len_q = len(queue)
            
            for i in range(len_q):
                node = queue.pop()
                if node:
                    right_side = node
                    queue.appendleft(node.left)
                    queue.appendleft(node.right)
            
            if right_side:
                right.append(right_side.val)
            
        return right