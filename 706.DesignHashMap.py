class MyHashMap(object):

    def __init__(self):
        self.table = {}

    def put(self, key: int, value: int) -> None:
        self.table[key] = value

    def get(self, key: int) -> int:
        if key in self.table: return self.table[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.table: del self.table[key]
