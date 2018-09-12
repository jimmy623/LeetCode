from collections import defaultdict

class Trie(object):
    def __init__(self):
        self.val = None
        self.count = 0
        self.nodes = defaultdict(Trie)


class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = Trie()
        for i,s in enumerate(sentences):
            self.append(s,i)
        self.inputs = []
        self.current = self.root

    def indexForChar(self,c):
        index = 0
        if c == " ":
            index = 1
        elif c == "#":
            index = 0
        else:
            index = ord(c) - ord("a") + 2
        return index

    def append(self,s,times):
        node = self.root
        
        for c in s:
            index = self.indexForChar(c)
            if not node.nodes[index]:
                child = Trie()
                child.val = c
                node.nodes[index] = child
            node.nodes[index].count += times
    

    def dfs(self,node,stack):
        if not node:
            return
        if node.val == "#":
            self.result.append("".join(self.inputs) + "".join(stack))
            if len(self.result) >= 3:
                return False
        stack.append(node.val)
        for n in node.nodes:
            if not self.dfs(n,stack):
                return False
        stack.pop()

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        self.inputs.append(c)
        if c == "#":
            self.append("".join(self.inputs),1)
            self.inputs = []
            self.current = self.root
        else:
            self.result = []
            index = self.indexForChar(c)
            if self.current:
                self.current = self.current.nodes[index]
                self.dfs(self.current,[])
            return self.result
sents = ["i love you","island","ironman","i love leetcode"]
times = [5,3,2,2]
s = AutocompleteSystem(sents,times)
print input("i")
print input(" ")
print input("a")
print input("#")




        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
#Design Search Autocomplete System
#https://leetcode.com/problems/design-search-autocomplete-system/description/