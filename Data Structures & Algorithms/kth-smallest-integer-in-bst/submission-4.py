# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        kth = 0
        def dfs(node):
            nonlocal count, kth
            if not node: return
            if count == k: return
        
            dfs(node.left)
            if count == k: return
            kth = node.val
            count += 1
            dfs(node.right)
        
        dfs(root)
        return kth
        