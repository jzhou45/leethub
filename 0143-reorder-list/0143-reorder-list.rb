# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {Void} Do not return anything, modify head in-place instead.
def reorder_list(head)
    arr = []
    node = head
    
    while node
        arr << node
        node = node.next
    end
    
    l, r = 1, arr.length - 1
    
    while l <= r
        head.next = arr[r]
        r -= 1
        head = head.next
        head.next = arr[l]
        l += 1
        head = head.next
    end
    
    head.next = nil
end