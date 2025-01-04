class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # More optimal solution TC: O(N + M), SC: O(1)
        # loops through both LL at the same time if they meet at a point in first iteration, loop exits and returns one of them, if there is no intersection for both, they'll both be None
        # and None is returned. But if one is longer than the other by a distance d, when we do that if one reaches None first it switches to the second LL and start traversing when the second reaches None to it switches 
        # to first and starts traversing. they end up being on same wavelength. use examples to try it out
        # from the other we find out that 
        # E.g if A is shorter by 2, it's pointer reaches None first and starts iterating on B, by the time B which is two step behind gets to Null and becomes beginning of A, they would meet at same wavelength and get to the intersection together
        currA = headA
        currB = headB

        while currA != currB:
            currA = headB if currA is None else currA.next
            currB = headA if currB is None else currB.next
        return currA


        # Checks the length of the two LL to determine which is longer then makes the pointer start at the same place by moving the longer one by the difference in their length
        # this puts that at the same level as the shorter one, if length are both the same initially, then diff is zero
        # then we iterate through both using two pointers to check the first occurence of which they match
        # TC: O(m + n + (m - n) + m + n) simplified into O(3m +n) or so, SC: O(N)


        currA, currB = headA, headB

        countA = self.countLength(currA)
        countB = self.countLength(currB)

        if countA > countB:
            return self.findCollision(currA, currB, countA - countB)
        else:
            return self.findCollision(currB, currA, countB - countA)


    def findCollision(self, curr1, curr2, diff):
        while diff > 0:
                curr1 = curr1.next
                diff -= 1
        while curr1 and curr2:
            if curr1 == curr2:
                return curr1
            curr1 = curr1.next
            curr2 = curr2.next
        
    def countLength(self, curr):
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count




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