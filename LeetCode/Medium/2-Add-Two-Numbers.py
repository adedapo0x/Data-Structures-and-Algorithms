class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        The approach is to use two pointers, one traversing through each LL, we create a dummy node for the sum LL
        Since the LL can be of varying length, one LL can reach its end before the other, so we make a loop using OR, as long as one of them is not Null
        A check is if the node exists, else, value of it is assigned zero. 
        Another check is done while updating pointers, this is to ensure we do not call the .next on a node that does not exist
        our while loop also checks if we have a carry at the last node we go through so we are able to add it to the dummy LL.
        Say addition of 8 + 7, sum is 15, node of 5 is created and linked, the carry being checked is needed else the loop stops and the 1 doesn't get linked
        '''
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            summ = v1 + v2 + carry
            carry = summ // 10
            val = summ % 10
            sumNode = ListNode(val)
            curr.next = sumNode

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
