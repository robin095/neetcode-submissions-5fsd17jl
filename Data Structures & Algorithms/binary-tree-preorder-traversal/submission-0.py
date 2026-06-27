# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        self._preorder(root, nodes)
        return nodes

    
    def _preorder(self, root, nodes):
        if not root:
            return
        nodes.append(root.val)
        self._preorder(root.left, nodes)
        self._preorder(root.right, nodes)

        