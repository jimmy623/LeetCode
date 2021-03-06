class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[None] = None

    def search(self, word):
        def find(word, node):
            if not word:
                return None in node
            char, word = word[0], word[1:]
            if char != '.':
                return char in node and find(word, node[char])
            return any(find(word, kid) for kid in node.values() if kid)
        return find(word, self.root)

wordDictionary = WordDictionary()
wordDictionary.addWord("word")
wordDictionary.addWord("abc")
wordDictionary.addWord("woed")

print wordDictionary.search("word")
print wordDictionary.search("wor")
print wordDictionary.search(".....")

#Add and Search Word - Data structure design
#https://leetcode.com/problems/add-and-search-word-data-structure-design/
