'''
Optimal solution is to use doubly linked list, models the actual tab navigation in browsers.  
a behaviour to note is that if we go back by a number of steps, and we then visit a new url, the former urls that we have visited at the front should
be cleared and the most recent is the url we just visited. this behaviour is the reason why using an array is not optimal, there is no constant time way to clear forward urls

TC: to initialize object and the visit operation is O(1)
    the back and forward has a TC of O(steps)
SC: O(N) where N is the number of urls visited.


Bruteforce approach is to use an array. [not implemented]
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev= None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = ListNode(homepage)
        self.curr = self.home
        
    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = node
        
    def back(self, steps: int) -> str:
        count = steps
        while count > 0 and self.curr != self.home:
            self.curr = self.curr.prev
            count -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        count = steps
        while count > 0 and self.curr.next:
            self.curr = self.curr.next
            count -= 1
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)