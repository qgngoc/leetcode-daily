# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def find_node(node, val):
    if not node:
        return None
    if node.val == val:
        return node
    left = find_node(node.left, val)
    if left:
        return left
    return find_node(node.right, val)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        visited = set()
        root = None
        current_root = None
        for i in range(len(inorder)):
            if inorder[i] not in visited:
                leftmosts = []
                for j in range(len(preorder)):
                    if preorder[j] in visited:
                        continue
                    visited.add(preorder[j])
                    leftmosts.append(preorder[j])
                    if preorder[j] == inorder[i]:
                        break
                if leftmosts:
                    left_subtree = TreeNode(val=leftmosts[0])
                    left_subtree_root = left_subtree
                    for node in leftmosts[1:]:
                        left_subtree.left = TreeNode(val=node)
                        left_subtree = left_subtree.left
                    # print(leftmosts)
                    # print(left_subtree_root)
                else:
                    # print("Leftmost empty")
                    left_subtree = None
                if not root:
                    current_root = left_subtree_root
                    root = current_root
                    while True:
                        if not current_root:
                            break
                        if not current_root.left:
                            break
                        current_root = current_root.left
                    # print(current_root, "+++")
                else:
                    current_root.right = left_subtree_root
                    current_root =  current_root.right
                    while True:
                        if not current_root:
                            break
                        if not current_root.left:
                            break
                        current_root = current_root.left
                    # print(current_root, '---')
            else:
                tmp_current_root = root
                current_root = find_node(tmp_current_root, inorder[i])
                # print(current_root, inorder[i])
        # print(root)
        return root
                    
