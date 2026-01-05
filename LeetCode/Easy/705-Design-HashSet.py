class MyHashSet:

    def __init__(self):
        self.myHash = set()
        
    def add(self, key: int) -> None:
        self.myHash.add(key)

    def remove(self, key: int) -> None:
        self.myHash.discard(key) # I use discard rather than remove here because remove would throw an error if key was not present

    def contains(self, key: int) -> bool:
        return key in self.myHash
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)