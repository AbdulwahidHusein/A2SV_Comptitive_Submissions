# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def height(root):
            if not root: return 0
            lheight = height(root.left)
            rheight = height(root.right)
            return max(lheight+1, rheight+1)
        h = height(root)
        ans = [[] for i in range(h)]

        def bfs(root, level, dist):
            nonlocal ans
            if not root: return
            if level == 0: 
                ans[dist].append(root.val)
                return
            bfs(root.left, level-1, dist+1)
            bfs(root.right, level-1, dist+1)
        for i in range(h):
            bfs(root, i, 0)

        res = []
        for i in range(h):
            if i%2 == 0:
                res.append(ans[i])
            else:
                res.append(reversed(ans[i]))
        return res