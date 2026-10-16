'''
Filter the BST by a range. Remove nodes that do not dall within this range
Similar intuition to solve this in LC 938
'''

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def filter_bst_by_range(root, min_val, max_val):
    if not root:
        return None

    # leverage the fact that since it is a BST, if the node value we are currently on is less than min, then we do not care about its left
    # subtree since it would also be lesser.
    # same for if node val is greater than max_val, the right subtree would be greater than max_val and therefore not in range.
    if root.val < min_val: 
        return filter_bst_by_range(root.right, min_val, max_val)
    if root.val > max_val:
        return filter_bst_by_range(root.left, min_val, max_val)
    
    new_node = Node(root.val)
    new_node.left = filter_bst_by_range(root.left, min_val, max_val)
    new_node.right = filter_bst_by_range(root.right, min_val, max_val)
    return new_node
