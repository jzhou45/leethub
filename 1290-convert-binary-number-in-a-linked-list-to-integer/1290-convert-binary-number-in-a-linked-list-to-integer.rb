# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {Integer}
def get_decimal_value(head)
    arr = []
    queue = [head]
    until queue.empty?
        node = queue.pop
        arr << node.val.to_s
        queue << node.next unless node.next.nil?
    end
    str = arr.join("").to_i(2)
end