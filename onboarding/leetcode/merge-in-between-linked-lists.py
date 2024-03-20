# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        templ = list1
        tempr = list1
        for _ in range(a-1):
            templ = templ.next
        for _ in range(b+1):
            tempr = tempr.next

        tail = list2
        while tail.next:
            tail = tail.next
        templ.next = list2
        tail.next = tempr
        return list1
        