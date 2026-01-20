# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor_p = []
        ancestor_q = []
        paths = []
        # paths_val
        stack_node = [root]
        stack_path = [[root.val]]
        while stack_node:
            node = stack_node.pop()
            path = stack_path[-1]
            stack_path = stack_path[:-1]
            if not node:
                continue
            if node == p or node == q:
                paths.append(path)
            if not node.left and not node.right:
                continue
            elif not node.right:
                stack_node.append(node.left)
                stack_path.append(path + [node.left.val])
            elif not node.left:
                stack_node.append(node.right)
                stack_path.append(path + [node.right.val])
            else:
                stack_node.append(node.left)
                stack_path.append(path + [node.left.val])   
                stack_node.append(node.right)
                stack_path.append(path + [node.right.val]) 

        path_p, path_q = paths[0], paths[1]
        path_q_set = set(path_q)
        common = 0
        for node in path_p:
            if node in path_q_set:
                common = node
                # break

        stack_node = [root]
        stack_path = [[root.val]]
        while stack_node:
            node = stack_node.pop()
            path = stack_path[-1]
            stack_path = stack_path[:-1]
            if not node:
                continue
            if node.val == common:
                return node
            if not node.left and not node.right:
                continue
            elif not node.right:
                stack_node.append(node.left)
                stack_path.append(path + [node.left.val])
            elif not node.left:
                stack_node.append(node.right)
                stack_path.append(path + [node.right.val])
            else:
                stack_node.append(node.left)
                stack_path.append(path + [node.left.val])   
                stack_node.append(node.right)
                stack_path.append(path + [node.right.val]) 
                  
        return None