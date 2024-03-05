# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        whp = defaultdict(lambda : [pow(2, 32), 0]) 
        mod = 2**32
        def dfs(node, n, h):
            if not node:
                return
            if whp[h][0] > n % mod: whp[h][0] = n %mod
            if whp[h][1] < n%mod: whp[h][1] = n%mod
            dfs(node.left, 2*n+1, h+1)
            dfs(node.right, 2*n+2, h+1)
        dfs(root, 0, 0)
        ans = 0
        for k in whp:
            ans = max(ans, whp[k][1] - whp[k][0])
        return ans + 1


