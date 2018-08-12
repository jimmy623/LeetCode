# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return "!"
        l = self.serialize(root.left)
        r = self.serialize(root.right)
        result = str(root.val) + "#" + l + "#" + r
        #print result
        return result
        
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        components = data.split("#")
        root = self.decodeWithComponents(components)
        return root
        
    def decodeWithComponents(self,comps):
    	#print comps
        if comps[0] == "!":
            del comps[0] 
            return None
        node = TreeNode(int(comps[0]))
        del comps[0] 
        node.left = self.decodeWithComponents(comps)
        node.right = self.decodeWithComponents(comps)
        return node
        
# c = Codec()
# root = TreeNode(-1)
# l = TreeNode(0)
# r = TreeNode(1)
# root.left = l
# root.right = r
# result = c.serialize(root)
# print result
# c.deserialize(result)
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))