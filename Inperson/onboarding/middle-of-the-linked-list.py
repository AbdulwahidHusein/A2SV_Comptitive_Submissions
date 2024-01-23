# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_count = 0
        temp = head
        while temp:
            temp = temp.next
            node_count += 1


        right_count = node_count // 2
        temp = head
        while temp and right_count > 0:
            right_count -= 1
            temp = temp.next

        return temp