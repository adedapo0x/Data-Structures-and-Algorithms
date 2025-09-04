class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Bruteforce way:
        # Will be to go through the LL, store the nodes in an array, then use two pointers
        # one at the beginning of the array, another at the end, then a loop, beginning points to end gets updated, end points to 
        # new updated beginning, end gets updated, repeat and repeat. all the while ensuring that left pointer remains less than right, once greater, break
        # TC: O(N), SC:O(N)

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        l,r =   0, len(nodes) - 1
        curr = head
        count = 0
        while l < r:
            count += 1
            if count % 2 != 0:
                curr.next = nodes[r]
                r -= 1
            else:
                l += 1
                curr.next = nodes[l]
            curr = curr.next
        curr.next  = None


        # Optimized way: TC: O(N), SC: O(1)
        # the algorithm is to divide the linked list into two, the first half stays the same 
        # the second half is reversed since we want our LL to consist of one from first half and one from second but starting from the end of the second
        # after splitting and sorting the second half, we merge them, no need to return anything since it is to be done inplace

        # to split, we use a slow and fast pointer, the slow shifts once each time, fast shifts twice each time
        # slow pointer starts from the first node, fast starts from the second node
        # if odd number of nodes in LL, fast being None means end of the LL stop loop, if even number of nodes, fast.next being None means they are no other nodes after fast and having one more iteration won't work as None has no .next 
        # where slow is at this point is the end of first LL, and slow.next is the beginning of second LL
        # you can try it out with examples e.g  1,2,3,4 or 1,2,3

        # think this works if you use slow = fast = head too, the goal is to just partition the LL, you can check it out with examples
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # after getting beginning of second LL, we reverse it
        second = slow.next
        slow.next = None # this makes end of first LL no longer point to beginning of second LL and points to None since we are dividing into two separates nodes
        prev = None
        while second:
            tempNext = second.next
            second.next = prev
            prev = second
            second = tempNext

        # now we merge it, prev holds the beginning of the reversed LL
        first, second = head, prev
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1,temp2 