"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        sub = []
        if root.children:
            sub = [self.serialize(child) for child in root.children]
        substring = "".join(sub)
        result = "{"+str(root.val) + ":" + "[" + substring + "]"+"}"
        # print result
        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not len(data):
            return None
        # print data
        i = data.index(":")
        val = int(data[1:i])
        childrenString = data[i+2:len(data)-2]
        childrenData = []
        stack = []
        start = 0
        for i in xrange(len(childrenString)):
            if childrenString[i] == "{":
                stack.append(i)
            elif childrenString[i] == "}":
                k = stack.pop()
                if len(stack) == 0:
                    childrenData.append(childrenString[k:i+1])

        children = []
        for cdata in childrenData:
            children.append(self.deserialize(cdata))
        return Node(val,children)

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

#Serialize and Deserialize N-ary Tree
#https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/description/