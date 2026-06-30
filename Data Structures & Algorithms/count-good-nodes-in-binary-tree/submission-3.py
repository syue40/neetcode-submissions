# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return []

        good_nodes = []
        def traverse(node, prev_nodes):
            nonlocal good_nodes
            if not node:
                return

            current_val = node.val
            print(current_val)
            print(prev_nodes)
            
            should_append = True
            for vals in prev_nodes:
                if vals > current_val:
                    should_append = False
                    break
            
            if should_append:
                good_nodes.append(current_val)

            # prev_nodes.append(current_val)

            if node.left:
                traverse(node.left, prev_nodes + [current_val])
            if node.right:
                traverse(node.right, prev_nodes + [current_val])

        traverse(root, [])
        return len(good_nodes)