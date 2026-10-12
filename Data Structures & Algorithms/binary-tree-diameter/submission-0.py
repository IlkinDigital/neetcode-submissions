# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = [0]

        self.search(root, max_diam)

        return max_diam[0]

    def search(self, root, max_diam):
        if not root:
            return 0

        left_height = self.search(root.left, max_diam)
        right_height = self.search(root.right, max_diam)

        max_diam[0] = max(max_diam[0], left_height + right_height)

        return 1 + max(left_height, right_height)