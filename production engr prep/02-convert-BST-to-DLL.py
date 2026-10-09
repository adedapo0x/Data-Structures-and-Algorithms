def bstToDoublyLinkedList(root):
    '''
    here we convert a BST to a circular doubly linked list. this is a LC premium question.
    so we use inorder traversal to go through the BST, since we get left, parent, right, and for a BST that gives us in its sorted format
    so all we have to do is to connect the nodes in place as we traverse in an inorder fashion, 
    use nonlocal so that we are accurately referencing the prev and head variables in the outer function
    since the DLL should be circular, after the traversal we then link the last node which would be held by prev and the head node to each other to make it circular

    TC: O(N), SC: O(H) where H is the height of the BST and is caused by the recursion stack used by the DFS
    for the H, worst case scenario, it can be O(N) if the BST is skewed, but in a balanced BST, it would be O(logN), so SC can be O(n) in worst case and O(logN) in best case
    '''
    prev, head = None, None
    
    def inorder(node):
        nonlocal prev, head
        if not node:
            return
        
        inorder(node.left)
        if not head:
            head = node
        else:
            node.left = prev
            prev.right = node
        prev = node
        inorder(node.right)
        
    inorder(root)
    prev.right = head
    head.left = prev
    return head