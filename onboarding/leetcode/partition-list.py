# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(0), ListNode(0)
        tempb, tempa = before, after
        
        while head:
            if head.val < x:
                tempb.next, tempb = head, head
            else:
                tempa.next, tempa = head, head
            head = head.next
        
        tempa.next = None
        tempb.next = after.next

        return before.next