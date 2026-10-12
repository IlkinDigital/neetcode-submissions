# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        encoded = ""

        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if not curr:
                    encoded += "null," 
                    continue
                encoded += str(curr.val) + ","

                queue.append(curr.left)
                queue.append(curr.right)
        
        if encoded[-1] == ",":
            encoded = encoded[0:len(encoded) - 1]

        return encoded
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "" or data == "null":
            return None
        
        n_data = data.split(",", )


        queue = deque()
        root = TreeNode(int(n_data[0]))
        queue.append(root)

        i = 1
        while len(queue) > 0 and i < len(n_data):
            curr = queue.popleft()

            if n_data[i] != "null":
                curr.left = TreeNode(int(n_data[i]))
                queue.append(curr.left)
            
            i += 1
            
            if n_data[i] != "null":
                curr.right = TreeNode(int(n_data[i]))
                queue.append(curr.right)

            i += 1
        
        return root



