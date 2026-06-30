# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p or queue_q:
            if len(queue_p) != len(queue_q):
                return False

            min_len = min(len(queue_p), len(queue_q))
            level_p = []
            level_q = []
            for i in range(min_len):
                p_node = queue_p.popleft()
                q_node = queue_q.popleft()

                level_p.append(p_node.val if p_node else None)
                level_q.append(q_node.val if q_node else None)

                if p_node:
                    queue_p.append(p_node.left)
                    queue_p.append(p_node.right)
                if q_node:
                    queue_q.append(q_node.left)
                    queue_q.append(q_node.right)

            if level_p != level_q:
                return False

        return True