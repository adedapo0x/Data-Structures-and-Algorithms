class MinStack:

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


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()