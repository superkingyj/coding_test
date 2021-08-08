class Trie:
    def __init__(self):
        self.root = {'dumy':None}

    def insert(self, word: str) -> None:
        pointer = self.root
        for char in word :
            if 'dumy' in pointer : 
                pointer[char] = {}
                del pointer['dumy']
            elif char not in pointer or not pointer : pointer[char] = {}
            else : pass
            pointer = pointer[char]

        pointer['\0']=None

    def search(self, word: str) -> bool:
        pointer = self.root
        for char in word :
            if 'dumy' in pointer or char not in pointer or not pointer: return False
            else : pointer = pointer[char]
        if '\x00' in pointer : return True
        return False

    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        for char in prefix:
            if 'dumy' in pointer or char not in pointer or not pointer: return False
            else : pointer = pointer[char]
        return True