# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if not root: return False
        target -= root.val
        if (target == 0 and not root.right and not root.left):
            return True
        return (self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target))
        