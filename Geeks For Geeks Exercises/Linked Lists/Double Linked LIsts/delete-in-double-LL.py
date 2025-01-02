'''
Given a Doubly Linked list and a position. The task is to delete a node from a given position (position starts from 1)
in a doubly linked list and return the head of the doubly Linked list

Input: LinkedList = 1 <--> 3 <--> 4, x = 3
Output: 1 <--> 3
Explanation: After deleting the node at position 3 (position starts from 1),the linked list will be now as 1 <--> 3.

'''

class Solution:
    def delete_node(self, head, x):
        curr = head
        count = 0
        if x == 1:
            prev = curr
            curr = curr.next
            prev.next = None
            curr.prev = None
            return curr
            
        while curr:
            count += 1
            if count == x: break
            curr = curr.next

        if not curr.next:
            prev = curr.prev
            prev.next = None
            curr.prev = None
        else:
            prev = curr.prev
            after = curr.next
            prev.next = prev.next.next
            curr.prev = None
            curr.next = None
            after.prev = prev
        return head
