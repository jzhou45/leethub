# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = [root.val]
        q = [root]
        
        while q:
            node = q.pop()
            if node.left:
                q.append(node.left)
                arr.append(node.left.val)
            if node.right:
                q.append(node.right)
                arr.append(node.right.val)

        arr.sort()
        res = float("inf")
        
        for i in range(len(arr) - 1, 0, -1):
            res = min(res, arr[i] - arr[i - 1])
        
        return res