# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        stack = []
        #add elements to the stack
        stack.append(head.val)
        temp = head
        while temp.next:
            stack.append(temp.next.val)
            temp = temp.next
        print(stack)
        temp = head
    
        while stack:
            if temp.val == stack.pop():
                pass
            else:
                return False
            temp = temp.next
        return True
        