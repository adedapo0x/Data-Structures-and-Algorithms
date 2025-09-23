class LRUCache:
    '''
    bruteforce approach
    the approach here is to use a hashmap as the cache to have O(1) lookup and insertion and use a list to maintain the order as elements are put or accessed
    we use a list to keep track of the order that way we can get the least recently used.
    so when we get a key, we remove it from the positon of order it is in our list, and append it to the end that way the last element is our most recent
    as for putting, if we have the key before in our cache, we remove it from its order cos its order should change considering it is now our most recent
    then we update our dict and list, after putting, if the capacity of the list is exceeded, we remove from the front of the list (since that is the least recently used)
    and delete from the dict since we do not want it in our system again

    TC: the time complexity for get and put becomes O(N) due to the remove operation of the list
    SC: O(N)
    '''
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.order = []
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value = self.cache[key]
        self.order.remove(key)
        self.order.append(key)
        return value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)

        self.cache[key] = value
        self.order.append(key)

        if len(self.cache) > self.cap:
            nodeToRemove = self.order[0]
            self.order.remove(nodeToRemove)
            del self.cache[nodeToRemove]