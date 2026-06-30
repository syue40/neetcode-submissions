# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # a search tree is valid if all the elements on the left are less than root
        # a search tree is valid if all the elements on the right are greater than root

        def check_is_valid(node, minimum, maximum):
            if not node:
                return True

            current_val = node.val
            if current_val >= maximum or current_val <= minimum:
                return False
            
            left_is_valid = check_is_valid(node.left, minimum, current_val)
            right_is_valid = check_is_valid(node.right, current_val, maximum)
            
            return left_is_valid and right_is_valid

        if not root:
            return True
        return (
            check_is_valid(root.left, -math.inf, root.val) and 
            check_is_valid(root.right, root.val, math.inf)
        )