# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = []

        self.search(root, visited, k)
        return visited[k - 1]


    def search(self, root, visited, k):
        if not root or len(visited) == k:
            return
        
        self.search(root.left, visited, k)
        visited.append(root.val)
        self.search(root.right, visited, k)