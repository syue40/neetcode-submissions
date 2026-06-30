# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []

        queue = deque([root])
        while queue:
            level = []
            q_len = len(queue)
            for _ in range(q_len):
                node = queue.popleft()
                node_val = node.val
                level.append(node_val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            output.extend(level)

        sorted_out = sorted(output)
        return sorted_out[k-1]