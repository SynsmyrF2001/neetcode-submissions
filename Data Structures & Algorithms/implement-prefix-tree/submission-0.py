class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
class PrefixTree:

    def __init__(self):
        """
        Initializes the prefix tree object.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts the string word into the prefix tree.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True


    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the prefix tree (i.e., was inserted before), and was false otherwise
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is a previously inserted string word that has the prefix, and false otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        
        