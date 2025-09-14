import random
class RandomizedSet:
    """
    we use an array and a dict here, more straightforward way would have been to use a set to get O(1) insertion and deletion, but we cannot get random from it
    so we combine data structures, array cos of random index we can work with to get random vals, and a hashmap and not a set, because we need O(1) lookup
    also with being able to link val in dict with that of array for efficient logic for O(1) removal to work

    to remove, we basically get the index in the array we want to remove from the dict, removal in array is O(N), we don't want that. so we basically move the element at the last to the position we want to pop
    from and pop the last element, say we have the array has [2, 10, 4, 6] and we want to remove 10 which is at index 1, so we make arr[1] equal to the last element ie arr[-1], so we now have
    [2, 6, 4, 6], then update the dict to reflect the new position of the val in the array ie 6 is now at index 1 not 3 anymore ,
    we can then pop the last element of the array which is O(1) operation and get [2, 6, 4] and delete the val we originally wanted to delete from the hash too.
    Order matters here, finish the updating and all before cleanup ie popping from the array,
    think this matters when the element we want to remmove is originally the last element, so if you pop before you update dict, and the array size reduces, you can get index out of bounds error

    random is basically, get random number between 0 and last index and return arr[that index]

    TC: O(1) at the expense of space, O(2N) = O(N)      
    """

    def __init__(self):
        self.arr = []
        self.hash = {}
        
    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        
        self.arr.append(val)
        self.hash[val] = len(self.arr) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False
        
        pos = self.hash[val]
        self.arr[pos] = self.arr[-1]
        self.hash[self.arr[pos]] = pos
        
        self.arr.pop()
        del self.hash[val]
        return True 
        
    def getRandom(self) -> int:
        randInd = random.randint(0, len(self.arr) - 1)
        return self.arr[randInd]
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()