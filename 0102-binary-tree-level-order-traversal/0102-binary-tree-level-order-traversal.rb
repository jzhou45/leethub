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
# @return {Integer[][]}
def level_order(root)
    return [] if root.nil?
    ret_val = []
    queue = [root]
    counter = 1
    rest_of_counter = 0
    temp = []
    until queue.empty?
        counter -= 1
        node = queue.shift
        temp << node.val
        unless node.left.nil?
            queue << node.left 
            rest_of_counter += 1
        end
        unless node.right.nil?
            queue << node.right 
            rest_of_counter += 1
        end
        if counter == 0
            ret_val << temp
            counter += rest_of_counter
            rest_of_counter = 0
            temp = []
        end
    end
    ret_val
end