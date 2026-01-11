# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
from collections import deque
import json
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        if root is None:
            return str([])
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                data.append(None)
                continue
            data.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        # print(json.dumps(data))
        return json.dumps(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print(data)
        data = json.loads(data)
        if not data:
            return None
        queue_data = deque(data)
        # queue_process = dequeue([])
        # queue_process.append(queue_data.popleft())
        root = TreeNode(val=queue_data.popleft())
        queue_node = deque([root])
        while queue_data and queue_node:
            node = queue_node.popleft()
            if node is None:
                continue
            left_val = queue_data.popleft()
            left = TreeNode(val=left_val) if left_val is not None else None
            right_val = queue_data.popleft()
            right = TreeNode(val=right_val) if right_val is not None else None
            node.left = left
            node.right = right
            queue_node.append(left)
            queue_node.append(right)
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))