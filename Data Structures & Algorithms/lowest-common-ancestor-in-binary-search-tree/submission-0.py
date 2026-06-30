# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = None

        def traverse(node):
            nonlocal ans
            if not node:
                return False
            
            current = node
            # 1. we need to first find p and q
            left = traverse(node.left)
            right = traverse(node.right)
            
            # 2. once we find p or q, we need to mark it as found
            found_one = current.val == p.val or current.val == q.val

            # 3. once both are found, we need to backtrack until 2 conditions are satisfied
            #   - left and right is true (indicating p and q are somewhere below)
            #   - left and mid (indicating p/q is below and current node is one of the items)
            #   - right and mid (indicating p/q is below and current node is one of the items)
            
            if (left and right) or (found_one and left) or (found_one and right):
                ans = current

            # indicates 
            return found_one or left or right
        
        traverse(root)
        return ans