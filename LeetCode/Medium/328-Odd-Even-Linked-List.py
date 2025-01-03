class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force approach, uses extra space to store nodes
        # TC: O(N), SC: O(N)
        if not head or not head.next:
            return head
        nodes = []
        temp = head
        while temp and temp.next:
            nodes.append(temp.val)
            temp = temp.next.next
        if temp: nodes.append(temp.val) # for odd number of nodes, might not add the last odd node
        temp = head.next
        while temp and temp.next:
            nodes.append(temp.val)
            temp = temp.next.next
        if temp: nodes.append(temp.val) # for even number of nodes, might not add the last even node
        temp = head
        i = 0
        # replaces the node values of the input LL, with the already ordered values in the array
        while temp:
            temp.val = nodes[i]
            i += 1
            temp = temp.next
        return head