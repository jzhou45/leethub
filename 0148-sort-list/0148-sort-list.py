# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        
        vals = []
        
        while node:
            vals.append(node.val)
            node = node.next
        
        vals = sorted(vals, reverse=True)
        
        res = head
        
        while head:
            head.val = vals.pop()
            head = head.next
        
        return res