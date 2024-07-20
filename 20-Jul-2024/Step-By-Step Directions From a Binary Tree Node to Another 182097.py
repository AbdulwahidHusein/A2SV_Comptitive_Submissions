# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start_path, end_path = [],[]
        def dfs(node, path):
            nonlocal start_path, end_path
            if not node:
                return
            if node.val == startValue:
                start_path = path[:]
            if node.val == destValue:
                end_path = path[:]
            path.append("L")
            dfs(node.left, path)
            path.pop()
            path.append("R")
            dfs(node.right, path)
            path.pop()

        dfs(root, [])
        start_path.reverse()
        end_path.reverse()
        while start_path and end_path and start_path[-1] == end_path[-1]:
            start_path.pop()
            end_path.pop()
        return "U" * len(start_path) + "".join(reversed(end_path))