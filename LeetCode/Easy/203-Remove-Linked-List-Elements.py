# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
        without using front and back two pointers approach. here we use only a pointer and we keep a dummy node that is connected to the head
        so we check the next element which is initially the head, if it has the value we do not want we move our .next pointer to the one after it. 
        and we do not move our curr until we get to a node that contains another value. 

        TC: O(N), SC: O(1)
        '''
        dummy = ListNode(-1, head)
        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next

        '''
        came up w this myself.
        Approach here is to use two pointers, one in front and one behind, so we use the front one to check if the val of the node is what we don't want so if it is we move it to the next node and
        connect our back node to that node. so if the node.val is not val, then we keep on going one node at a time for both front and back.
        I am having to do an explicit check "if front" before I move the front and back pointers, because if the last node in the LL has the value we do not want,
        front then becomes None inside our inner while loop, and we do not want to call a .next on None, that throws an error

        TC: O(N), SC: O(1)
        '''
        dummy = ListNode(-1, head)
        back, front = dummy, head

        while front:
            while front and front.val == val:
                front = front.next
                back.next = front

            if front:
                front = front.next
                back = back.next

        return dummy.next
    

        # The bruteforce would be to go through the LL, and appending nodes that their values are not val into a list, then we then iterate through
        # the list connecting the nodes pointers to one another, and we can then return the first node in the list
        # TC: O(N), SC: O(N)



    
