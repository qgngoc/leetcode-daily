# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depths = set()
        def traverse(node, depth):
            global max_depth
            if not node:
                return
            depths.add(depth)
            traverse(node.left, depth+1)
            traverse(node.right, depth+1)
        traverse(root, 0)
        return max(depths) + 1