# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        node = dummy.next
        node2 = head
        
        counter = 0
        
        while node:
            counter += 1
            node = node.next
            
        if counter == 0:
            return None
            
        counter2 = 0
            
        if counter // 2 == 0:
            counter2 = counter / 2 - 2
        else:
            counter2 = (counter + 1) / 2 - 2
            
        while counter2 >= 0:
            node2 = node2.next
            counter2 -= 1
            
        if node2.next:
            if node2.next.next:
                node2.next = node2.next.next
            else:
                node2.next = None
        else:
            node2.next = None
            
        return dummy