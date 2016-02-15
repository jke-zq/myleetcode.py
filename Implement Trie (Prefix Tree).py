class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isstring = False
        self.nodes = {}
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for c in word:
            if c not in p.nodes:
                p.nodes[c] = TrieNode()
            p = p.nodes[c]
        p.isstring = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for c in word:
            if c in p.nodes:
                p = p.nodes[c]
            else:
                return False
        return p.isstring

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for c in prefix:
            if c in p.nodes:
                p = p.nodes[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

##import --simplify the codes