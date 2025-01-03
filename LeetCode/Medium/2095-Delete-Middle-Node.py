class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        More optimal approach, only one pass, we use fast and slow pointers
        Create a dummy node and point its next to head, slow is at dummy, fast is at head
        then traverse fast twice, slow once, at the end of LL, slow is at just the node before the middle node and we adjust its next pointer
        We return dummy.next and not head, cos if it is just one node, we remove it we can't return the head, we returning dumm.next that now points to None
        TC: O(N), SC: O(N)
        '''
        dummy = ListNode(0, head)
        slow = dummy
        fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return dummy.next

        # Uses counting. Done in two passes. First pass, counts the number of nodes in the LL
        # then we find the mid and traverse to the node before the mid and adjust its next pointer
        # TC: O(N), SC:0(1)
        if not head.next:
            return None
        curr = head
        count = -1
        while curr:
            count += 1
            curr = curr.next
        print(count)
        mid = math.ceil(count / 2)
        curr = head
        count2 = -1
        while curr:
            count2 += 1
            if count2 == mid - 1:
                break
            curr = curr.next
        print(curr.val)
        curr.next = curr.next.next
        return head