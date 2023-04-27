# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head 
        counter = 1
        p1, p2 = head, None

        # one moving our p1 n away from the start 
        while counter < n: 
            p1 = p1.next 
            counter += 1

        p2 = head 
        prev = dummy 
        # two incremeneting both of our points 
        while p1.next: 
            p1 = p1.next 
            prev = p2 
            p2 = p2. next 
            print(p1.val, p2.val,prev.val)
        # third removing node
        prev.next = p2.next 
        return dummy.next 