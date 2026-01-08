# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None, current_sum=None, max_sum=None):
        self.val = val
        self.left = left
        self.right = right
        self.current_sum = current_sum
        self.max_sum = max_sum

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        current_sums = []
        def assign_current_sum(node):
            current_sum = None
            max_sum = None
            if not node.right and not node.left:
                current_sum = node.val
                max_sum = node.val
                node.current_sum = current_sum
                node.max_sum = max_sum
            elif not node.right and node.left:
                assign_current_sum(node.left)
                current_sum = node.val + max(node.left.max_sum, 0)
                max_sum = node.val + max(node.left.max_sum, 0)
                node.current_sum = current_sum
                node.max_sum = max_sum
            elif node.right and not node.left:
                assign_current_sum(node.right)
                current_sum = node.val + max(node.right.max_sum, 0)
                max_sum = node.val + max(node.right.max_sum, 0)
                node.current_sum = current_sum
                node.max_sum = max_sum
            else:
                assign_current_sum(node.left)
                assign_current_sum(node.right)
                current_sum = node.val + max(node.left.max_sum, 0)+ max(node.right.max_sum, 0)
                max_sum = node.val + max(node.left.max_sum, node.right.max_sum, 0)
                node.current_sum = current_sum
                node.max_sum = max_sum
            # max_current_sum = max(node.current_sum, max_current_sum)
            # print(node, node.max_sum ,node.current_sum)
            current_sums.append(node.current_sum)
        assign_current_sum(root)

        return max(current_sums)