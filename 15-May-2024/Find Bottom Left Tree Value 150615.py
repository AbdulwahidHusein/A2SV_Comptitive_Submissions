# Problem: Find Bottom Left Tree Value - https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        while q:
            curr = []
            for _ in range(len(q)):
                node = q.popleft()
                curr.append(node)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

        return curr[0].val
