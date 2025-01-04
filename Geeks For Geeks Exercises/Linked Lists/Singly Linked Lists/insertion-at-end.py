'''
Given the head of a Singly Linked List and a value x, insert that value x at the end of the LinkedList and return the modified Linked List.
'''

class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        if not head:
            return Node(x)
        curr = head
        while curr.next:
            curr = curr.next
        node = Node(x)
        curr.next = node
        return head
