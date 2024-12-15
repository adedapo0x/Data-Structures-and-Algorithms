# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # creates a dummy node whose next is the beginning of our merged LL, since we cannot get the head normally
        # checks and compares the value of each node since the merged LL must be ascending in order
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # here for if one of the list is None initially, so we can just direct the dummy next pointer to the one that has elements
        # also for when looping, one of either list1 or list2 can end up being None first, this connects tail next to the one that remains of what still has elements

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
