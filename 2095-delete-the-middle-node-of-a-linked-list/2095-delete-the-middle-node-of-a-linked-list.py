# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        node = dummy.next
        
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
            dummy = dummy.next
            counter2 -= 1
            
        if dummy.next:
            if dummy.next.next:
                dummy.next = dummy.next.next
            else:
                dummy.next = None
        else:
            dummy.next = None
            
        return head