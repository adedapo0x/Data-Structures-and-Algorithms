class MyHashMap:

    def __init__(self):
        self.myHash = {}
        

    def put(self, key: int, value: int) -> None:
        self.myHash[key] = value
        

    def get(self, key: int) -> int:
        return self.myHash[key] if key in self.myHash else -1
        
    def remove(self, key: int) -> None:
        if key in self.myHash:
            del self.myHash[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)