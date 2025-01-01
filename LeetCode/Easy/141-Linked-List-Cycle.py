class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # uses two pointers, TC: O(N), SC: O(1)
        # so if a cycle exists, the pointers would at a point meet, else the fast pointer becomes null and the loop ends
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False




        # TC: O(N), SC: O(N)
        # Uses an hashset to store the previously visited nodes
        # We could also use curr.next in hashSet to check for values
        hashSet = set()
        curr = head
        while curr:
            if curr in hashSet:
                return True
            hashSet.add(curr)
            curr = curr.next
        return False