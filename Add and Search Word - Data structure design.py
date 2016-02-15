class TrieNode(object):
    def __init__(self):
        self.isstring = False
        self.nodes = {}

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if c not in cur.nodes:
                cur.nodes[c] = TrieNode()
            cur = cur.nodes[c]
        cur.isstring = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                oldroot = self.root
                for node in cur.nodes.values():
                    self.root = node
                    if self.search(word[i + 1:]):
                        self.root = oldroot
                        return True
                self.root = oldroot
                return False
            elif c in cur.nodes:
                cur = cur.nodes[c]
            elif '.' in cur.nodes:
                cur = cur.nodes['.']
            else:
                return False
        return cur.isstring

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

##import:bad codes, using DFS templet