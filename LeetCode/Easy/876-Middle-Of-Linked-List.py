class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Uses two pointers method, fast and slow pointer, fast moves two nodes a time, slow one node at a timr
        # while fast and fast.next is to know when to stop for both odd and even number of nodes
        # TC: 0(N), SC: 0(1)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
        



        # Iterates through the loop twice, first to get the number of nodes in the LL
        # then divide by 2, integer division plus one, run it through test cases, it works
        # then iterate again till our middle is zer0, that gives us the node at the middle
        # TC: 0(N), SC: 0(1) 

        # count = 0
        # curr = head
        # while curr:
        #     count += 1
        #     curr = curr.next
        # mid = (count // 2) + 1
        # curr = head
        # while curr:
        #     mid -= 1
        #     if mid == 0:
        #         return curr
        #     curr = curr.next