class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.freq = 0
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_Word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.freq += 1

    def search_Word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                print("False")
                return 
            node = node.children[char]
        print(node.is_end)
    
    def query(self, prefix, k):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        results = []
        self._collect(node, prefix, results)

        results.sort(key=self.sort_key)
        return results[:k]

    def sort_key(self, item):
        word, freq = item
        return (-freq, word)

    def _collect(self, node, prefix, results):
        if node.is_end:
            results.append((prefix, node.freq))
        for char, child in node.children.items():
            self._collect(child, prefix + char, results)

    def remove_Word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return
            node = node.children[char]
        if node.is_end:
            if node.freq > 1:
                node.freq -= 1
            else:
                node.is_end = False
                node.freq = 0

if __name__ == '__main__':
    root = Trie()

    root.add_Word("Apple")
    root.add_Word("Apple")
    root.add_Word("App")
    root.add_Word("Application")

    print("Initial:")
    print(root.query("App", 5))

    root.remove_Word("Apple")
    print("\nAfter remove Apple once:")
    print(root.query("App", 5))

    root.remove_Word("Apple")
    print("\nAfter remove Apple twice:")
    print(root.query("App", 5))


    