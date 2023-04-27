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
def count_nodes(root)
    return 0 if root.nil?
    accum = 0
    queue = [root]
    until queue.empty?
        node = queue.shift
        accum += 1
        queue << node.left unless node.left.nil?
        queue << node.right unless node.right.nil?
    end
    accum
end