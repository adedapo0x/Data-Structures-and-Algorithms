class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

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
