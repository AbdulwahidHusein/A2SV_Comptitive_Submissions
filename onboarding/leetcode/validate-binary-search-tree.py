# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(root, min_v, max_v):
            if root is None:
                return True
            if root.val >= max_v or root.val <= min_v:
                return False
            is_leftV = bst(root.left, min_v,  root.val)
            is_rightV = bst(root.right, root.val, max_v)
            return is_leftV and is_rightV

        return bst(root, -float('inf'), float('inf'))