class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node
    def insert(self, word: str) -> None:
        nodes = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not nodes.children[ch]:
                nodes.children[ch] = Trie()
            nodes = nodes.children[ch]
        nodes.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    trie.search("apple")
