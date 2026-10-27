'''
    297. Serialize and Deserialize Binary Tree
    
    Serialize: Use level order traversal to serialize the binary tree into a string representation.
    Deserialize: Use the serialized string to reconstruct the binary tree using a queue to keep track of the nodes.
    
    Time Complexity: O(n) for both serialization and deserialization, where n is the number of nodes in the binary tree.
    Space Complexity: O(n) for both serialization and deserialization, as we store the serialized string and use a queue to reconstruct the tree.
'''

# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized = []
        serialized.append(str(root.val) if root else 'None')
        q = deque([root])
        
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur:
                    if cur.left:
                        serialized.append(str(cur.left.val))
                        q.append(cur.left)
                    else:
                        serialized.append('None')
                    
                    if cur.right:
                        serialized.append(str(cur.right.val))
                        q.append(cur.right)
                    else:
                        serialized.append('None')
                    
        
        return ','.join(serialized)
                    
                    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(',')
        n = len(values)
        if n == 0 or values[0] == 'None':
            return None
        
        root = TreeNode(int(values[0]))
        
        i = 1
        q = deque([root])
        
        while q:
            cur = q.popleft()
            if i < n and values[i] != 'None':
                cur.left = TreeNode(int(values[i]))
                q.append(cur.left)
            i += 1
            if i < n and values[i] != 'None':
                cur.right = TreeNode(int(values[i]))
                q.append(cur.right)
            i += 1

        return root
        

# Test case
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5) 

ser = Codec()
deser = Codec()
ans = ser.serialize(root)
print(ans)  # Output: "1,2,3,None,None,4,5,None,None,None,None"

print(type(deser.deserialize(ans)))  # Output: The original binary tree structure