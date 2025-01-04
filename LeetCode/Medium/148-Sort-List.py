class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 


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