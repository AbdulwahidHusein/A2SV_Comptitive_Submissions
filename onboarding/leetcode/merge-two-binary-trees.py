# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root2:
            return root1
        if not root1:
            return root2

        merged = TreeNode()

        def merge(root1, root2, parent, direct):
            newNode = TreeNode()
            if not root1 and not root2:
                return 
            if root1 and not root2:
                newNode.val = root1.val
                root2 = TreeNode()
            elif root2 and not root1:
                newNode.val == root2.val
                root1 = TreeNode()
            if root1 and root2:
                newNode.val = root1.val + root2.val
            if direct == "left":
                parent.left = newNode
            else:
                parent.right = newNode
            merge(root1.left, root2.left, newNode, "left")
            merge(root1.right, root2.right, newNode, "right")
        merged.val = root1.val + root2.val
        merge(root1.left, root2.left, merged, "left")
        merge(root1.right, root2.right, merged, "right")
        return merged