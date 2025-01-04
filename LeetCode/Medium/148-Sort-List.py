class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # uses merge sort to the LL itself
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = head
        right = mid.next
        mid.next = None

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left,right)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left,right):
        dummy = ListNode()
        tail = dummy
        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return dummy.next


        # used extra space here to convert LL to list, sort then, insert values back
        # TC: O(nlogn), SC: O(N)
        if not head: return head
        nodes = []
        curr = head
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        nodes.sort()
        curr = head
        curr.val = nodes[0]
        sortedHead = curr
        i = 1
        curr = curr.next
        while curr:
            curr.val = nodes[i]
            i += 1
            curr = curr.next
        return sortedHead