# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative method TC: O(N), SC: O(1)
        current = head
        prev = None
        while current:
            nexxt = current.next
            current.next = prev
            prev = current
            current = nexxt
        return prev
    

        # recursive method, TC: O(N), SC: O(N)
        def reverse(head, prev=None):
            if head is None:
                return prev
            nexxt = head.next
            head.next = prev
            return reverse(nexxt, head)
        return reverse(head)

        