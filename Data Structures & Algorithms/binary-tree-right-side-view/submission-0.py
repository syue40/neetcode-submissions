# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])

        output = []
        while queue:
            q_len = len(queue)

            for i in range(q_len):
                item = queue.popleft()
                if i == q_len - 1:
                    output.append(item.val)

                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)

        return output