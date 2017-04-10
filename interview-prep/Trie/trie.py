#Simple implementation of a trie
class Trie():
    class TrieNode():
        def __init__(self):
            self.children = {}
            self.end_of_word = False

    def __init__(self,):
        self.root = self.TrieNode()

    def __str__(self):
        print(self.root.children)

    def insert(self,word):
        curr = self.root
        for char in word:
            node = curr.children.get(char,-1)
            if node == -1:
                node = self.TrieNode()
                curr.children[char] = node
            curr = node
        curr.end_of_word = True

    def search(self,word):
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return curr.end_of_word == True

    def starts_with(self,prefix):
        curr = self.root
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return True


# trie = Trie()
# trie.insert("cax")
# trie.__str__()
# print(trie.starts_with(""))
# # print(trie.search("caxr"))
