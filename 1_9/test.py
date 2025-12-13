class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def display(self):
        self._display(self.root, '')
    
    def _display(self, node, prefix):
        if node.is_end:
            print(prefix)
        for ch, child in node.children.items():
            self._display(child, prefix + ch)

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                print("False")
                return
            node = node.children[char]
        print(node.is_end)

if __name__ == '__main__':
    root = Trie()
    root.insert("Apple")
    root.insert("Banana")
    root.display()

    root.search("apple")
    root.search("Apple")
    root.search("App")
    root.search("app")

