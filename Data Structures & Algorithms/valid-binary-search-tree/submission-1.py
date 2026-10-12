# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, (-math.inf, math.inf))

    def valid(self, root, valid_range):
        if not root:
            return True

        if root.val <= valid_range[0] or root.val >= valid_range[1]:
            return False

        return self.valid(root.left, (valid_range[0], root.val)) and self.valid(root.right, (root.val, valid_range[1]))