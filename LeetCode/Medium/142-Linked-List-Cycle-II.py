class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # uses that Floyd hare and snail cycle detection algorithm
        # TC: O(N), SC: O(1)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # finds where both fast and slow pointers meet on the same node
                break
        else: return None # for if the LL is empty or contains only one node

        slow2 = head
        while slow2 != slow: # starts another loop from the beginning of the LL, point where they meet is the beginning of the cycle
            slow = slow.next
            slow2 = slow2.next
        return slow
    
        # another way of doing this is to use set, as we traverse through the LL, if the node isn't already in the set that means we haven't seen it before
        # then we add it to the set, if we come across a node already in the set, that means that there is a cycle and that node is the beginning of the cycle
        # else we return None after traversing if no previously seen node was come across
        # TC: O(N), SC: O(N)