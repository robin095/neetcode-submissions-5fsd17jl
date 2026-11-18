# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        seen = []
        cur = root
        while cur:
            seen.append(cur)
            cur = cur.left
        while seen or cur:
            last = seen.pop()
            res.append(last.val)
            if last.right:
                cur = last.right
                while cur:
                    seen.append(cur)
                    cur = cur.left
        
        return res
        