class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # optimal solution
        # Uses two pointers, odd and even
        # odd goes through connecting odd together, even does the same for even nodes
        # we need a variable for even head in order to the link the tail of odd to after the loop is done
        # we use even and even.next as the condition because of even is always after odd so no need checking for odd too
        if not head or not head.next:
            return head
        odd, even = head, head.next
        evenHead = head.next
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenHead
        return head


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