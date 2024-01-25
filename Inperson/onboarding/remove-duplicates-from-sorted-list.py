# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = temp
        while temp:
            if temp.val != prev.val:
                prev.next = temp
                prev = temp
            temp = temp.next
        if prev:
            prev.next = temp
        return head