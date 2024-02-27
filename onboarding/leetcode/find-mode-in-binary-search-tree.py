# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        c = Counter()
        def dfs(root):
            nonlocal c
            if not root:
                return
            c[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        common = c.most_common()
        max_c = common[0][1]
        ans = []
        for n, f in common:
            if f == max_c:
                ans.append(n)
        return ans
