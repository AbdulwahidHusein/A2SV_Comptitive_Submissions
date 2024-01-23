# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        prev = None
        current = head
        nextt = current.next
        while current != None:
            current.next = prev
            prev = current
            current = nextt
            if not nextt is None:
                nextt = nextt.next
        return prev


        