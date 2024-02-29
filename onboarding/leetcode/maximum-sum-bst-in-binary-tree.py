# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def LRcondition(self, node, left_max, right_min):
        if left_max >= node.val:
            return False
        if right_min <= node.val:
            return False
        return True
    def dfs(self, node):
        if node is None:
            return [0, float("inf"), float("-inf")]

        l, minl, maxl = self.dfs(node.left)
        r, minr, maxr = self.dfs(node.right)

        if self.LRcondition(node, maxl, minr) and  l != "n" and r != "n":
            self.ans = max(self.ans, l + r + node.val)
            _min = min(minl, minr, node.val)
            _max = max(maxl, maxr, node.val)

            return [l + r + node.val, _min, _max]
        return ["n", node.val, node.val]
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
