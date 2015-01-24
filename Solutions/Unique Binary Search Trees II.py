# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return "Node value:"+str(self.val)

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        results = []
        if n == 0:
            return [None]
        r = self.generate(range(1,n+1))
        return r
  
    def generate(self,vals):
        if len(vals) == 0:
            return [None]
            
        if len(vals) == 1:
            node = vals[0]
            return [TreeNode(node)]
        
        length = len(vals)
        result = []
        
        for i in range(length):
            root = vals[i]
            lvals = vals[0:i]
            rvals = vals[i+1:length]
            left = self.generate(lvals)
            right = self.generate(rvals)
            for l in left:
                for r in right:
                    rNode = TreeNode(root)
                    rNode.left = l
                    rNode.right = r
                    result.append(rNode)
        return result
            
    def serializeTree(self,root):
        if root == None:
            return []
        remain = [root]
        result = [root.val]
        while len(remain):
            n = remain[0]

            remain.remove(n)
            if n.left == None and n.right == None:
                continue
            
            if n.left:
                result.append(n.left.val)
                remain.append(n.left)
            else:
                result.append("#")
            
            if n.right:
                result.append(n.right.val)
                remain.append(n.right)
            else:
                result.append("#")
            
            if result[-1] == "#":
                result = result[0:len(result)-1]
        return result
        

    
s = Solution()
r = s.generateTrees(3)
print r



#Unique Binary Search Trees II
#https://oj.leetcode.com/problems/unique-binary-search-trees-ii/