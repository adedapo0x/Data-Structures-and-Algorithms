'''
You are given an array nodes. It contains 7 integers, which represents the value of nodes of the binary tree
in level order traversal. You are also given a root of the tree which has a value equal to nodes[0].

Your task to construct a binary tree by creating nodes for the remaining 6 nodes.
'''

class Node:
    # had to write the Node class myself btw
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
class Solution:
    def createTree(self, root, l):
        # probably cleaner and more efficient way to do this than what I have here, lmao
        a = root
        a.left = Node(l[1])
        a.right = Node(l[2])
        
        b = a.left
        b.left = Node(l[3])
        b.right = Node(l[4])
        
        c = a.right
        c.left = Node(l[5])
        c.right = Node(l[6])