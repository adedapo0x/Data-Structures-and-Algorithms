'''
Another approach is to use a dynamic array, just like a list in python. sliightly better TC but use more memory I think

so here we use a single array to keep track of all the visited sites, while efficiently manipulating indexes, initially our array has only the homepage in it,
and currentUrlPos and threshold are set to zero. currentUrlPos is the index at which we are at currently, while threshold is the index to which we still 
have valid sites. anything beyond threshold is not to be considered as part of how history

to visit, we check if the size of the array can already accomodate that new index (would be because of a former back operation), if so, just change that index in the array
to the new site to be visited, else if the array is not yet big enough, then just append that url to the list, then update threshold to be on that last index visited
to go back, we can do this in O(1) time, which is the advantage of this approach, we can directly access the index, by subtracting, if the steps are too high and we get negative,
that is wy we take the max of both, in that case, we have 0 and we can then access visited[0]
for forward, similar thing, we do not go beyond the threshold, so we take the min of the sum of currentUrlPos and steps, and the threshold, so 
whichever is smaller, we update our currentUrlPos there, this makes sure we never go out of bounds of threshold

more memory can be said to be used here, eg
[leetcode.com, bloomberg.com, amazon.com,  google.com], to go back 2 steps from google (index 3), we do 3 - 2, which is 1, so we are at bloomberg
and because we could potentially visit another site and clear amazon and beyond, we set our threshold back to 1, so say we decide to visit apple.com from bloomberg,
we simply update amazon to apple, and threshold is now 2, so although google.com remains in the array, we cannot consider it because it is beyond the threshold
so on a larger scale, we can end up with a lot of sites to the right of our array that we can no longer access, hence more memory consumption

TC: O(1) for all operations
SC: O(N)
'''
class BrowserHistory:

    def __init__(self, homepage: str):
        self.visited = [homepage]
        self.currentUrlPos = 0
        self.threshold = 0

    def visit(self, url: str) -> None:
        self.currentUrlPos += 1
        if len(self.visited) > self.currentUrlPos:
            self.visited[self.currentUrlPos] = url
        else:
            self.visited.append(url)
        self.threshold = self.currentUrlPos

    def back(self, steps: int) -> str:
        self.currentUrlPos = max(self.currentUrlPos - steps, 0)
        return self.visited[self.currentUrlPos]

    def forward(self, steps: int) -> str:
        self.currentUrlPos = min(self.currentUrlPos + steps, self.threshold)
        return self.visited[self.currentUrlPos]



'''
One solution is to use doubly linked list, models the actual tab navigation in browsers.  
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