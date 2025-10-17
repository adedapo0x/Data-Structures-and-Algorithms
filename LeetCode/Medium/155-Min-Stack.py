class MinStack:
    # One stack approach, the stack stores both the val and the current minimum at that point in time
    # we use a tuple to store (val, currMin). if stack is empty and we want to push, we can just say val is for now the minimum and do (val, val)
    # better to use a tuple instead of a list because they are immutable and we do not want to mistakenly change the currMin at a pparticular time, this should be fixed
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            currMin = self.stack[-1][1]
            self.stack.append((val, min(val, currMin)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


    # Two stacks approach

    def __init__(self):
        # initalize two stacks, second one in order to enable getting min value in O(1) time.
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # compare val to know if there is a new minimum
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val) # append new minimum to minStack


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # returns last element in minStack since minStack just records minimum values
        return self.minStack[-1]
    

    # The bruteforce of this problem, has an O(N) for getMin, we take a temp stack, and a mini initialized to the top of the self.stack
    # then we keep on comparing with the top of the stack as we pop the values from self.stack and append to temp, then we append back to self.stack,
    # the values from temp, in order to return the stack to its original state


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()