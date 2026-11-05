# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def min_value_node(self, root):
            cur = root
            while cur and cur.left:
                cur = cur.left
            return cur
        

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_right_node = self.min_value_node(root.right)
                root.val = min_right_node.val
                root.right = self.deleteNode(root.right, min_right_node.val)
        return root
