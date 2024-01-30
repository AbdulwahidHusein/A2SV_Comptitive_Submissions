# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #the ugly way
        if n == 1 and not head.next:
            return None
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        length -= (n + 1)
        temp = head
        if length < 0:
            return temp.next
        for i in range(length):
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next
        return head