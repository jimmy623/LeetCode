#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.route = []
        self.current = None
        
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.current == None:
            if self.root:
                return True
            return  False
            
        h = len(self.route) - 1
        while h >= 0:
            if self.route[h].val > self.current.val:
                return True
            h -= 1
        
        if self.current.right != None:
            return True
        return False

    # @return an integer, the next smallest number
    def next(self):
        if self.current == None:
            iter = self.root
            self.route.append(iter)
            while iter.left != None:
                iter = iter.left
                self.route.append(iter)
            self.current = iter
            return iter.val
            
        while len(self.route):
            if self.route[-1].val > self.current.val:
                self.current = self.route[-1]
                return self.current.val
            elif self.route[-1].right != None and self.route[-1].right.val > self.current.val:
                iter = self.route[-1].right
                self.route.append(iter)
                while iter.left != None:
                    iter = iter.left
                    self.route.append(iter)
                self.current = iter
                return iter.val
            else:
                self.route.remove(self.route[-1])
            
                

#Your BSTIterator will be called like this:
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)

three.left = one
one.right = two
three.right = four

i, v = BSTIterator(three), []

while i.hasNext():
    val = i.next()
    print val
    v.append(val)



#Binary Search Tree Iterator 
#https://oj.leetcode.com/problems/binary-search-tree-iterator/