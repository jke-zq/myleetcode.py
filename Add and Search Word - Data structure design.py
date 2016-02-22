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
        def searchRec(word, pos, node):
            if pos == len(word):
                return node.isstring
            else:
                if word[pos] in node.nodes:
                    return searchRec(word, pos + 1, node.nodes[word[pos]])
                elif word[pos] == '.':
                    for n in node.nodes.values():
                        if searchRec(word, pos + 1, n):
                            return True
                    return False
                else:
                    return False
        cur = self.root
        return searchRec(word, 0, cur)

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

##import:bad codes, using DFS templet