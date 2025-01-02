'''
Given a doubly linked list. Your task is to reverse the doubly linked list and return its head.
'''

class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        curr = head
        prev = None
        while curr:
            after = curr.next
            curr.next = prev
            curr.prev = after
            prev = curr
            curr = after
        return prev