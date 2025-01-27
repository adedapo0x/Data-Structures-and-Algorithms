# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. 
# The function should return the total sum of all values in the linked list.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# uses recursive method this time around
def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)
