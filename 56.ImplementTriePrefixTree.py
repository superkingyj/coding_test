import collections
# set end possible
# dictionary function
# __init__(char)

# TrieNode 95
class CharNode:
    def __init__(self):
        self._isEnd = False
        self._charNodes = collections.defaultdict(CharNode)
    
    def getNext(self, char):
        return self._charNodes[char]
    
    def setEnd(self):
        self._isEnd = True

    def isIn(self, char):
        return char in self._charNodes
    
    def isEnd(self):
        return self._isEnd

class Trie:
    def __init__(self):
        self.root = CharNode()

    def insert(self, word: str) -> None:
        pointer = self.root
        for char in word :
           pointer = pointer.getNext(char)
        pointer.setEnd()

    def search(self, word: str) -> bool:
        pointer = self.root
        for char in word :
            if not pointer.isIn(char): return False
            pointer = pointer.getNext(char)
        return pointer.isEnd()

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        for char in prefix:
            if not pointer.isIn(char): return False
            pointer = pointer.getNext(char)
        return True
    
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")
