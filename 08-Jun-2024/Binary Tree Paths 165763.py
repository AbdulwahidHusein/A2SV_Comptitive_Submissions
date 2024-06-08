# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(node, curr):
            if not node:
                return
            if not node.left and not node.right:
                curr.append(str(node.val))
                ans.append(curr[:])
            curr.append(str(node.val))
            dfs(node.left, curr[:])
            dfs(node.right, curr[:])

        dfs(root, [])
        return ["->".join(path) for path in ans]