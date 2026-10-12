# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right = []

        queue = deque()
        if root:
            queue.append(root)
            
        while len(queue) > 0:
            val = 0
            for _ in range(len(queue)):
                curr = queue.popleft()
                val = curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            right.append(val)

        return right