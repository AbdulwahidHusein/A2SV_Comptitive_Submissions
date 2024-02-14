class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        part_size = length // k
        remaining_parts = length % k
        
        res = []

        node = head
        for _ in range(k):
            curr_size = part_size
            if remaining_parts > 0:
                curr_size += 1
                remaining_parts -= 1
            starting_head = node
            for _ in range(curr_size - 1):
                if node:
                    node = node.next
            if node:
                next_node = node.next
                node.next = None
                node = next_node
            res.append(starting_head)
        return res