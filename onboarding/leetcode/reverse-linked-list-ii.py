# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        emp = ListNode(0)
        emp.next = head
        left_node = emp
        
        for i in range(left - 1):
            left_node = left_node.next
        
        right_node = left_node.next
        
        for i in range(right - left):
            next_node = right_node.next
            right_node.next = next_node.next
            next_node.next = left_node.next
            left_node.next = next_node

        return emp.next
