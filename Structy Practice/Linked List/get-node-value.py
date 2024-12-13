# Write a function, get_node_value, that takes in the head of a linked list and an index. 
# The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# iterative way
def get_node_value(head, index):
  count = 0
  current = head
  while current is not None:
    if index == count:
      return current.val
    current = current.next
    count += 1
  return None


# recursive way
def get_node_value(head, index):
  if head is None:
    return None
  if index == 0:
    return head.val
  return get_node_value(head.next,index-1)
    