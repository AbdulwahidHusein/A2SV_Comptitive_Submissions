# Problem: Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return
        ans = []
        s = set(to_delete) 
        def rec(node, isf, parent=None, dir=None):
            if not node:
                return
            if node.val in s:
                if parent:
                    if dir == "l":
                        parent.left = None
                    else:
                        parent.right = None

                rec(node.left, True, node, 'l')
                rec(node.right, True, node, 'r')
                return
   
            if isf:
                ans.append(node) 
            rec(node.left, False, node, 'l')
            rec(node.right, False, node, 'r')
        rec(root, True)
        return ans