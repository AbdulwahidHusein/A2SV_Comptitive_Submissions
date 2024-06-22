# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path):
            path.append(str(node.val))
            if not node.left and not node.right:
                return
            if not node.left:
                path.append("()")
                path.append("(")
                dfs(node.right, path)
                path.append(")")
                return
            if not node.right:
                path.append("(")
                dfs(node.left, path)
                path.append(")")
                return
            path.append("(")
            dfs(node.left, path)
            path.append(")")
            path.append("(")
            dfs(node.right, path)
            path.append(")")
        path = []
        dfs(root, path)
        return "".join(path) 