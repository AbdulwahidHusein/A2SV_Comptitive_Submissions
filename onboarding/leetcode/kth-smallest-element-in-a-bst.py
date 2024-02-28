from typing import Optional
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        min_heap = []
        count = 0

        def dfs(node):
            nonlocal count
            if node is None:
                return

            dfs(node.left)
            count += 1
            if len(min_heap) < k:
                heapq.heappush(min_heap, -node.val)
            elif node.val < -min_heap[0]:
                heapq.heappushpop(min_heap, -node.val)
            dfs(node.right)

        dfs(root)
        return -min_heap[0]