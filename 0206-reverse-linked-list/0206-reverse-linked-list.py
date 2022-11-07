# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        res = dummy
        while dummy:
            dummy.val = arr.pop()
            dummy = dummy.next
        return res