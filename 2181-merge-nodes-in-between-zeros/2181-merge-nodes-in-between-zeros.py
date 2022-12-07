# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_sum = 0
        res = ListNode()
        res.next = ListNode(val=0)
        node = res.next
        
        while head:
            if head.val == 0 and curr_sum > 0:
                node.next = ListNode(val=curr_sum)
                node = node.next
                curr_sum = 0
            else:
                curr_sum += head.val
            head = head.next
        
        return res.next.next