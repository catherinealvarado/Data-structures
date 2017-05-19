class Node:
    """
    Implementation of node for trie.
    """
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie(object):
    """
    This is an implementation of a trie.
    """

    def __init__(self):
        self.root = Node()

    def __str__(self):
        """Prints all of the starting nodes in trie."""
        print(self.root.children)

    def insert(self,word):
        """Inserts a word into trie."""
        curr = self.root
        for char in word:
            node = curr.children.get(char,-1)
            if node == -1:
                node = Node()
                curr.children[char] = node
            curr = node
        curr.end_of_word = True

    def search(self,word):
        """Checks to see if a word is in trie."""
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return curr.end_of_word == True

    def starts_with(self,prefix):
        """Checks if a prefix is in the trie."""
        curr = self.root
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return True

#This is intantiating an instance of a Trie class
# trie = Trie()
# trie.insert("cax")
# trie.__str__()
# print(trie.starts_with(""))
# print(trie.search("cax"))
