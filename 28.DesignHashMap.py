class MyHashMap(object):

    def __init__(self):
        self.size = 100000
        self.table = list([0 for i in range(self.size)])

    def put(self, key: int, value: int) -> None:
        hashValue = self.hashFunction(key)
        node = NodeList(key, value)

        if self.table[hashValue] == 0 :
            dumy = NodeList()
            self.table[hashValue] = dumy
            dumy.next = node
            return
        
        pointer = self.table[hashValue]
        prev = pointer.prev
        while True :
            if not pointer: 
                pointer = node
                node.prev = prev
                if prev:
                    prev.next = node
                return
            elif pointer and pointer.key == key:
                pointer.value = value
                return
            prev = pointer
            pointer = pointer.next
        
    def get(self, key: int) -> int:
        hashValue = self.hashFunction(key)

        if self.table[hashValue] == 0 :
            return -1
        
        pointer = self.table[hashValue]
        while True:
            if not pointer:
                return -1
            elif pointer.key == key:
                return pointer.value
            else :
                pointer = pointer.next
 
    def remove(self, key: int) -> None:
        hashValue = self.hashFunction(key)

        if self.table[hashValue] == 0:
            return -1
        
        pointer = self.table[hashValue]
        prev = pointer.prev
        while True:
            if not pointer:
                return -1
            elif pointer.key == key:
                prev.next = pointer.next
                if pointer.next:
                    pointer.next.prev = prev
                pointer = None
                return
            else :
                prev = pointer
                pointer = pointer.next

    def hashFunction(self, key: int) -> int:
        hashValue = key % self.size
        return hashValue

class NodeList :
    def __init__(self, key=None, value=None) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


# class MyHashMap(object):

#     def __init__(self):
#         self.table  = {}

#     def put(self, key: int, value: int) -> None:
#         self.table[key] = value

#     def get(self, key: int) -> int:
#         if key in self.table:
#             return self.table[key]
#         return -1

#     def remove(self, key: int) -> None:
#         if key in self.table:
#             del self.table[key]