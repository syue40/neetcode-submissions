# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_dist = 0

        def dfs(node):
            nonlocal largest_dist
            if not node:
                return 0

            left_dist = dfs(node.left)
            right_dist = dfs(node.right)

            sum_dist = left_dist + right_dist
            left_or_right = max(left_dist, right_dist)
            largest_dist = max(largest_dist, sum_dist)

            return left_or_right + 1

        dfs(root)
        return largest_dist