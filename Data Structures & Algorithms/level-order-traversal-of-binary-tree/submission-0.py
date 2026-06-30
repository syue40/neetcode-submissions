# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # for level order traversal, we should use a queue
        if not root:
            return []

        queue = [(root, 0)]
        output = []
        while len(queue) > 0:
            current, level = queue.pop()

            try:
                output[level].insert(0, current.val)
            except Exception:
                output.append([])
                output[level].insert(0, current.val)
            
            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))
            
        return output
