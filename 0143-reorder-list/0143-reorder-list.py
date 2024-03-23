from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = deque([])
        tail = head.next

        while tail:
            stack.append(tail)
            tail = tail.next

        tail = head

        while stack:
            if stack:
                popped = stack.pop()
                popped.next = None
                tail.next = popped
                tail = tail.next
            if stack:
                popped = stack.popleft()
                popped.next = None
                tail.next = popped
                tail = tail.next
        
        return head
        