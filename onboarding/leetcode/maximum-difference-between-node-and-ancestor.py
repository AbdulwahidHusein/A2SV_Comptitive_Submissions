# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, min_ancestor, max_ancestor):
            nonlocal ans
            if node is None:
                return
            ans = max(ans, abs(min_ancestor - node.val), abs(max_ancestor - node.val))

            min_ancestor = min(min_ancestor, node.val)
            max_ancestor = max(max_ancestor, node.val)

            dfs(node.left, min_ancestor, max_ancestor)
            dfs(node.right, min_ancestor, max_ancestor)

        dfs(root.left, root.val, root.val)
        dfs(root.right, root.val, root.val)
        return ans