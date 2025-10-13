"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:

    """
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    '''
    iterative and intuitive solution, just prioritize if there is a child, we store the .next node in a stack and put that node to its child node, then make its .child pointer None
    the stack is to keep track of all the next nodes that we have previously seen in the correct order as we saw them, so once we get to an end we can pop from the stack and connect that 
    node to our curr

    TC: O(N), SC: O(N)
    '''
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        curr = head
        stack = []

        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            if not curr.next and stack:
                nextNode = stack.pop()
                curr.next = nextNode
                nextNode.prev = curr
            curr = curr.next
        return head
    




    '''
    We use recursion (DFS) to go through the LL. our recursive function takes prev and curr, two nodes that we want to connect to each other
    we check for a child before we try to connect to next, if child doesn't exists, we return and we then go with next
    if it does, we explore the child connecting the nodes as we go, when we get to an end, ie a node without child or next, that is a tail and we keep on returning it 
    as we go up in order to connect that one with the next node that we have stored in tempNext

    TC: O(N) where N is the total number of nodes in the LL
    SC: O(N) due to recursion stack space
    '''
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        dummyHead = Node(None, None, head, None)
        self.flattenLL(dummyHead, head)
        
        head.prev = None
        return head


    def flattenLL(self, prev, curr):
        if not curr:
            return prev

        prev.next = curr
        curr.prev = prev

        tempNext = curr.next
        tail = self.flattenLL(curr, curr.child)
        curr.child = None
        return self.flattenLL(tail, tempNext)




    
        