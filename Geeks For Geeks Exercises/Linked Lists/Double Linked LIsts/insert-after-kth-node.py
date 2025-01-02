'''
Given a doubly-linked list, a position p, and an integer x. The task is to add a new node with value x at the position just after pth node in the doubly linked list 
and return the head of the updated list
'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        if not head:
            return Node(x)
        count = -1
        curr = head
        while curr:
            count += 1
            if count == p: break
            curr = curr.next
        after = curr.next
        node = Node(x)
        node.next = after
        node.prev = curr
        curr.next = node
        return head