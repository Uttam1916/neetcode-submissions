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
            return "N"
        s=[]
        nodes=deque()
        nodes.append(root)

        while nodes:
            node=nodes.popleft()
            if not node:
                s.append("N")
            else:
                s.append(str(node.val))
                nodes.append(node.left)
                nodes.append(node.right)
            


        return ",".join(s)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if vals[index]!="N":
                node.left=TreeNode(int(vals[index]))
                queue.append(node.left)
            index+=1
            if vals[index]!="N":
                node.right=TreeNode(int(vals[index]))
                queue.append(node.right)
            index+=1
        return root
