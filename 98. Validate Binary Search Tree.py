# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def is_sorted(arr):
  for i in range(len(arr) - 1):
    if arr[i] >= arr[i + 1]:
      return False
  return True

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inodr_arr = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            inodr_arr.append(node.val)
            traverse(node.right)
        
        traverse(root)
        return is_sorted(inodr_arr)