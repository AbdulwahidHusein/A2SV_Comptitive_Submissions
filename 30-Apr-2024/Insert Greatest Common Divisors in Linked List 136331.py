# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp and temp.next:
            val1 = temp.val
            next_node = temp.next
            val2 = next_node.val
            node = ListNode(gcd(val1, val2))
            
            node.next = next_node
            temp.next = node
            temp = next_node
        return head