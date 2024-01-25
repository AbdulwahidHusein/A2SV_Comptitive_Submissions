class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        temp_ans = ans
        temp1 = list1
        temp2 = list2

        while temp2 and temp1:
            if temp1.val < temp2.val:
                node = temp1
                temp1 = temp1.next
            else:
                node = temp2
                temp2 = temp2.next
            temp_ans.next = node
            temp_ans = temp_ans.next

        while temp1:
            node = temp1
            temp1 = temp1.next
            temp_ans.next = node
            temp_ans = temp_ans.next
        while temp2:
            node = temp2
            temp2 = temp2.next
            temp_ans.next = node
            temp_ans = temp_ans.next
        return ans.next