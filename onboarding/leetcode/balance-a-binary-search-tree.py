# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        self.nodes.append(node)
        self.inorder(node.right)
    def construct(self, nums):
        n = len(nums)
        if n == 0:
            return None
        root = nums[n//2]
        root.left = self.construct(nums[:n//2])
        root.right = self.construct(nums[n//2+1:])
        return root
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.nodes = []
        self.inorder(root)
        return self.construct(self.nodes)