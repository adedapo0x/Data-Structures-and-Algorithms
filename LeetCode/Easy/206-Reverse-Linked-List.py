# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative method TC: O(1), O(N)
        current = head
        prev = None
        while current:
            nexxt = current.next
            current.next = prev
            prev = current
            current = nexxt
        return prev
    

       

        