# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = {}
        
        queue = [root]
        
        while queue:
            node = queue.pop()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
                
            count[node.val] = count.get(node.val, 0) + 1
        
        curr_max = 0
        res = []
        
        for k, v in count.items():
            if v > curr_max:
                curr_max = v
                res = [k]
            elif v == curr_max:
                res.append(k)
        
        return res