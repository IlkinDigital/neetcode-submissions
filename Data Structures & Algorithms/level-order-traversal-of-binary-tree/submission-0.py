# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        self.search(root, 0, levels)
        return levels

    def search(self, root, level, levels):
        if not root:
            return
            
        if level + 1 > len(levels):
            levels.append([root.val])
        else:
            levels[level].append(root.val)

        self.search(root.left, level + 1, levels)
        self.search(root.right, level + 1, levels)

