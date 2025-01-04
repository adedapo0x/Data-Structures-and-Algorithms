class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # uses set to note if it has previously been seen
        # goes through one LL storing that the nodes in the set, then traverses through the other one, checking for the first node to have been previoulsy seen
        # TC: O(m + n), SC: O(m)

       hashB = set()

        currB = headB
        while currB:
            hashB.add(currB)
            currB = currB.next
        currA = headA
        while currA:
            if currA in hashB:
                return currA
            currA = currA.next
        return None