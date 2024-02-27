# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        tnode = None
        def dfs(node):
            nonlocal tnode
            if not node:
                return None
            if node.val == val:
                tnode = node
                return
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return tnode