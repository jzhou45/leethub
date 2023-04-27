# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer}
def sum_of_left_leaves(root)
    count = 0
    return count if root.nil?
    queue = [root]
    until queue.empty?
        node = queue.shift
        count += node.left.val if leaf?(node.left)
        queue << node.left unless node.left.nil?
        queue << node.right unless node.right.nil?
    end
    count
end

def leaf?(node)
    return false if node.nil?
    return true if node.right.nil? && node.left.nil?
    false
end 