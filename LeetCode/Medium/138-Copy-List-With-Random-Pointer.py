class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        ''' More Optimal Solution (TC: O(N), SC: O(1)) # SC: O(N) not considering the new LL that the question requires us to make
            This approach removes the use of an hashmap, that the former solution below makes use of. The copy of the nodes are stored directly after the original nodes in the input LL by manioulating the next pointers
            On the first pass, we create a copy of each node and we make the original node point to it, then the copy points to the next original node. Process is repeated till we get to the end of the LL
            So at this stage, we have originalA -> copyA -> originalB -> copyB -> originalC...
            Second pass takes care of the random pointers, if it doesn't point to None, we make the copy's random pointer point to the next node after where the original random points to (with our logic, this will be a copy of a node)
            if None, we can just make it point to None
            On the third pass, we create a dummy node in order to link our copies next pointer to form the LL to be returned. So dummy points to nearest copy and original points to its next original node as it was initially
            Then we return dummy.next as it is the first copy and the beginning of the deep copy LL
        '''

        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = curr.next.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
            curr = curr.next.next

        dummy = Node(-1)
        temp = dummy
        curr = head
        while curr:
            temp.next = curr.next
            curr = curr.next.next
            temp = temp.next

        return dummy.next



        ''' Two Pass with HashMap (TC: O(N), SC: O(N))
            This approach makes use of an hashmap to store the nodes with it's copy in the first pass. This is because the random pointer could be pointing to nodes
            that we haven't gotten to yet. On the first pass we create a copy of each node in the input LL, storing original node as key and copy of node as value
            On second pass, we set the next pointer of copy to the value of the original node next pointer in the hashMap. that is {X: x, Y: y} and X.next is Y, we know that x.next is going to be y,
            so to achieve this since curr is representing original nodes (e.g X), it's .next is a key in hashMap so we get it's value for x.next since key is original, value is copy
            Same goes for random also. Note: We instantiate hashmap with None:None because if random or next pointers point to None, we do not have it in the hashMap. This takes care of that edgecase
            Then we return value of the head since it'll be it's copy and the beginning of the deep copy '''
        oldToCopy = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]
