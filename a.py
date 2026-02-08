# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def get_node_max_depth(root):
    max_depth = -1
    def traverse(node, depth):
        nonlocal max_depth
        if not node:
            return
        if not node.left and not node.right:
            max_depth = max(max_depth, depth)
        traverse(node.left, depth + 1)
        traverse(node.right, depth + 1)
    traverse(root, 0)
    return max_depth

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(get_node_max_depth(root.left) - get_node_max_depth(root.right)) > 1:
            return False
        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False
        return True