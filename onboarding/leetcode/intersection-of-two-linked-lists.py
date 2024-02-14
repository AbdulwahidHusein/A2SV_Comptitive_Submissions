# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB
        while temp1:
            temp1.val = -temp1.val
            temp1 = temp1.next
        ans = None
        while temp2:
            if temp2.val < 0:
                ans = temp2
                break
            temp2 = temp2.next
        t = headA
        while t:
            t.val = - t.val
            t  = t.next
        return ans