# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        The approach here is quite simple conceptually, we use a dummy node at the start of the linked list that connects to the head. we use this as our first groupPrev, ie the node
        before the group of size k we are currently considering, we then get the kth node using an helper function getKthNode, note that to get kthNode we start from the groupPrev
        and not the beginning of the group in order not to miss it by one node. after getting kth node, we also store the node after it in groupNext, ie the node after the group we are currently looking at

        since we now have the beginning and the end of the group, beginning from groupPrev.next and end from kthNode
        initially, we keep our curr at groupPrev.next since that is the start of the group, we also keep prev as groupNext instead of the normal None we would usually do when reversing a LL normally,
        this is because after the reversal is complete, from the examples, we see that what was previously the start would point to groupNext after reversal since it would be at the end, so convenient to just set its .next
        now. we keep reversing until we get to groupNext, that signifies we are done with that group and need to stop reversing

        what remains now is to adjust relevant pointers, groupPrev was initially pointing to the start of the LL, but after reversing the group we need it to point to what was the end of the group initially i.e the kthNode,
        but before we update its .next, remember that we also need to move our groupPrev in order to be able to reverse the next group, so we need to update it to just before the start of the next group,
        since we have reversed, this would be what groupPrev was initially pointing to. so we need to store that in a temp variable first 
        and then we can return dummy.next

        TC: since we have N nodes and k group, each group is N / k, and for each node that we traverse, we reverse ie O(k)
        so TC is (N/k) x k which leaves us with O(N)
        SC: O(1) 
        '''
        dummy = ListNode(-1, head)
        groupPrev = dummy

        while True:
            kthNode = self.getKthNode(groupPrev, k)
            if not kthNode:
                break
            groupNext = kthNode.next

            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = temp

        return dummy.next


    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        

        '''
        Bruteforce way of solving this, just store the nodes in a list, and reverse in groups of k, then merge all of them together as a LL
        by connecting their .next to the next one as they are now ordered the way we want them
        TC is O(N), SC: O(N)
        '''

        if k == 1:
            return head

        nodes = []
        curr = head
        # putting the nodes in a list
        while curr:
            nodes.append(curr)
            curr = curr.next

        # reversing k by k 
        for i in range(0, len(nodes), k):
            if i + k <= len(nodes):
                nodes[i:i+k] = reversed(nodes[i:i+k])

        # connecting the nodes to one another
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]
        nodes[-1].next = None # making sure the last node points to null
        return nodes[0]