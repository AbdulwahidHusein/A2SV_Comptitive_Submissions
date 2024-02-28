# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        pos = defaultdict(list)
        def dfs(node, col, row):
            nonlocal pos
            if not node:
                return
            pos[(col, row)].append((node.val))
            dfs(node.left,  col-1, row+1)
            dfs(node.right, col+1, row+1)
            
        dfs(root, 0, 0)
        skv = sorted(pos.items(), key=lambda x: x[0])
        offset = 0
        max_ = 0
        for y in skv:
            offset = min(offset, y[0][0])
            max_ = max(max_, y[0][0])
            y[1].sort()
        ans = [ [] for _ in range( (max_ - offset + 1))]
        for y in skv:
            ans[y[0][0] - offset].extend(y[1])
        #print(skv)
        return ans
