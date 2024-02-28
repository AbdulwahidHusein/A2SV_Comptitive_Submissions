# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def des(node, path):
            nonlocal ans
            if not node.left and not node.right:
                path.append(str(node.val))
                ans += int("".join(path))
                return
            path.append(str(node.val))
            if node.left:
                des(node.left, path.copy())
            if node.right:
                des(node.right, path.copy())
        des(root, [])
        return ans
