# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return "#"
        
        # Pre-order traversal
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def build_tree(nodes):
            val = next(nodes)
            if val == "#":
                return None
            
            node = TreeNode(int(val))
            node.left = build_tree(nodes)
            node.right = build_tree(nodes)
            return node

        # Split the string and use an iterator to consume values
        nodes = iter(data.split(','))
        return build_tree(nodes)