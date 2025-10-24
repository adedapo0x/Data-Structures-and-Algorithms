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
        



'''
Another way to do this is to use two stacks and a current variable. one stacks holds history, when we visit new sites, we put the previous currents there
then the other stack is future, for when we want to go back and forth to store the ones that are ahead as we go back

to initialize, our homepage is set to current, when we visit a site, we want to put our current in the history stack and then set our current to this new url that 
we want to visit. to go back, we basically start appending to future as we pop from current, then to go forward, we append to history as we pop from forward
also, not that for visit, we want to clear future each time, cos in case we were on leetcode in the sequence, leetcode -> facebook -> instagram, visiting another site from
leetcode clears facebook and instagram

TC: for visit, O(1), for back and forward, O(min(m,n)) where m is the m is the maximum number of steps to og forward or backword and n is the number of visit calls made.
SC: O(N)
'''
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = []
        self.future = []
        self.current = homepage
        
    def visit(self, url: str) -> None:
        self.history.append(self.current)
        self.current = url
        self.future = []
        
    def back(self, steps: int) -> str:
        count = 0
        while count < steps and self.history:
            count += 1
            self.future.append(self.current)
            self.current = self.history.pop()
        return self.current

    def forward(self, steps: int) -> str:
        count = 0
        while count < steps and self.future:
            count += 1
            self.history.append(self.current)
            self.current = self.future.pop()

        return self.current




# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)