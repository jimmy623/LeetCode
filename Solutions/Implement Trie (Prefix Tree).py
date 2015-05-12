class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.value = ""
        self.nodes = []

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        p = self.root
        for c in word:
            result = None
            for n in p.nodes:
                if n.value == c:
                    result = n
                    break
            if result:
                p = result
            else:
                new = TrieNode()
                new.value = c
                p.nodes.append(new)
                p = new
        end = TrieNode()
        p.nodes.append(end)
        
                

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        p = self.root
        for c in word:
            result = None
            for n in p.nodes:
                if n.value == c:
                    result = n
                    break
            if result:
                p = result
            else:
                return False
        for n in p.nodes:
            if n.value == "":
                return True
        return False
        

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        p = self.root
        for c in prefix:
            result = None
            for n in p.nodes:
                if n.value == c:
                    result = n
                    break
            if result:
                p = result
            else:
                return False
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
#Implement Trie (Prefix Tree)
#https://leetcode.com/problems/implement-trie-prefix-tree/