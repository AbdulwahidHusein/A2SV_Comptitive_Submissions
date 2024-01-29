class Solution:
   def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       if not head: 
           return head
    
       odd = head
       even = head.next
       even_start = head.next
       while even and even.next:
           odd.next = odd.next.next
           odd = odd.next
           even.next = even.next.next
           even = even.next

       odd.next = even_start

       return head