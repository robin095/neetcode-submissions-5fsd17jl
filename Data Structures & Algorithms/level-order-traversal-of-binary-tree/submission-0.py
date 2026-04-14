# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        expected_output = []
        if root:
            queue.append(root)
            expected_output.append([root.val])
        while len(queue) > 0:
            nested_queue = []
            for i in range (len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    nested_queue.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    nested_queue.append(curr.right.val)
            if len(nested_queue) > 0:
                expected_output.append(nested_queue)
        return expected_output


        
        