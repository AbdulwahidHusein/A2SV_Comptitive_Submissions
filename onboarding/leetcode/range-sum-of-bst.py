# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_ = 0
        def dfs(node):
            nonlocal sum_
            if node is None:
                return sum_
            if node.val <= high and node.val >= low:
                sum_ += node.val
            dfs(node.right)
            dfs(node.left)
        dfs(root)
        return sum_
            