class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:
    '''
    Optimal approach is to use a doubly linked list to maintain the order rather than a list. Still the same ordering tho, most recently used would be at the end of the linked list
    and least frequently used will be at the start. so when we get or put, we adjust in the LL

    in the dict, we store the key given as the key and the node representing that key in the LL. the node would contain the key, value with both prev and next pointers
    we created a Node object by ourselves up. we also need dummy head and tail, so we can immediately tell the first element when we want to remove the LRU using the dummyHead.next,
    and also get the last node in the LL went we want to put a node as our most recent by doing dummyTail.prev. 

    we also create helper functions removeNode and addToBack.
    removeNode removes the node from its position in the LL, ie it connects what was before and after the node together, so the node is no longer in between them
    the addToBack is used to update our order as the most recently used, so we connect last node before dummy tail to it and connect it with the dummy tail, effectively making it the new last
    node before the dummy tail

    TC: O(1), SC: O(N)
    '''

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.dummyHead = Node(0, 0)
        self.dummyTail = Node(0, 0)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        value = node.val
        self.removeNode(node)
        self.addToBack(node)

        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
            self.addToBack(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.addToBack(node)

            if len(self.cache) > self.cap:
                nodeAfterHead = self.dummyHead.next
                self.removeNode(nodeAfterHead)
                nodeAfterHead.next = nodeAfterHead.prev = None
                del self.cache[nodeAfterHead.key]

    def removeNode(self, node):
        after, prev = node.next, node.prev
        prev.next = after
        after.prev = prev

    def addToBack(self, node):
        tailPrev = self.dummyTail.prev
        tailPrev.next = node
        node.prev = tailPrev
        node.next = self.dummyTail
        self.dummyTail.prev = node



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