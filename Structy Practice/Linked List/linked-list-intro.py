class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# hardcoding a linked list for learning purposes

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d

# method to iteratively traverse through a linked list and print its values
def print_ll(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next

# method to recursively traverse through a linked list and print its values
def recursive_printll(head):
    if head is None:
        return
    print(head.val)
    recursive_printll(head.next)


# print_ll(a)

# recursive_printll(b)


