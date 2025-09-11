class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # one pass method, creates dummy and uses two pointers O(N)
        # logic could have been to keep the distance between left and right pointers by n, so when the right is None means left pointer is at the node we want to delete
        # but this way we have no way of accessing previous node to change where it points to
        # so we use a dummy node at the beginning, make distance be n + 1, that case when right reaches None, left is one node before the one we intend to delete
        # so we just next it to the one after the to be deleted one
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # gets right pointer to be n nodes away from head, the left being at dummy then makes distance n + 1
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:  # moves the pointers till right becomes Null
            left = left.next
            right = right.next

        left.next = left.next.next # actual redirection of node occurs
        return dummy.next #returns head


        # a two pass method of O(N) TC would be to reverse the LL, then delete from the front
        # this is a two pass algorithm, can be done in one pass


        # slightly better bruteforce, we do one pass here, only issue is the extra space we use
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        if len(nodes) == 1:
            return None

        pos = len(nodes) - n 

        if pos == 0: # this occurs if n is len(nodes), so they want us to remove the first element
            return head.next

        nodes[pos - 1].next = nodes[pos].next # skips the particular node, we are looking for, no need to 
        return head
    



        # bruteforce solution(came up with this)
        # stores nodes in array, then pass through once again skipping the nth one
        # TC: O(N), SC: O(N)
        # edge case at end of code...
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        pos = len(nodes) - n
        dummy = ListNode()
        curr = dummy
        for i in range(len(nodes)):
            if i == pos:
                continue
            curr.next = nodes[i]
            curr = curr.next

        if n == 1: # if what to deleted is last node, make the node before it point to None unless it'll still 
            curr.next = None  # point to it since it doesn't have anything after to otherwise point to
        
        return dummy.next