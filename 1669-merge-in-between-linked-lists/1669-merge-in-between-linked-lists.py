# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = end = None
        count = 0
        node = list1
        
        while node:
            if count == a - 1:
                start = node
            elif count == b:
                end = node
            node = node.next
            count += 1
        
        node2 = list2

        while list2.next:
            list2 = list2.next
        
        list2.next = end.next
        
        start.next = node2
        
        return list1