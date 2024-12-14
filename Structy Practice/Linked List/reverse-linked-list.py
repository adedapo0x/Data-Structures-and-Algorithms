# Write a function, reverse_list, that takes in the head of a linked list as an argument.
# The function should reverse the order of the nodes in the linked list in-place 
# and return the new head of the reversed linked list.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_list(head):
    # better more straightforward method (iterative method)
    # TC: O(N, SC: O(1)
    current = head
    prev = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

# recursive method
def reverse_list(head, prev=None):
    if head is None:
        return prev
    next = head.next
    head.next = prev 
    return reverse_list(next, head)
  


# not optimal approach, uses TC of O(N+N) = O(N), SC = O(N)
# def reverse_list(head):
#   temp = []
#   current = head
#   while current is not None:
#     temp.append(current.val)
#     current = current.next

#   current = head
#   for i in range(len(temp) -1, -1, -1):
#     current.val = temp[i]
#     current = current.next

#   return head
    
    
    
    
