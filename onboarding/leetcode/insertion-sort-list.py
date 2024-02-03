class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        sorted_head = head
        temp = head.next
        sorted_head.next = None  

        while temp:
            stemp = sorted_head
            newNode = ListNode(temp.val)

            if temp.val < stemp.val:
                newNode.next = sorted_head
                sorted_head = newNode
            else:
                prev = None
                while stemp and newNode.val >= stemp.val:
                    prev = stemp
                    stemp = stemp.next

                newNode.next = stemp
                prev.next = newNode

            temp = temp.next

        return sorted_head