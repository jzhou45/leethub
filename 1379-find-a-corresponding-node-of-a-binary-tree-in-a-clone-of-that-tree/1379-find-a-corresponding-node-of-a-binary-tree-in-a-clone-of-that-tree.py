# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        arr = [original]
        move_path = [cloned]
        while len(arr) != 0:
            node = arr[0]
            cloned_node = move_path[0]
            if node.left != None:
                arr.append(node.left)
                move_path.append(cloned_node.left)
            if node.right != None:
                arr.append(node.right)
                move_path.append(cloned_node.right)
            if node == target:
                break
            arr.pop(0)
            ret_val = move_path.pop(0)
        return move_path[0]