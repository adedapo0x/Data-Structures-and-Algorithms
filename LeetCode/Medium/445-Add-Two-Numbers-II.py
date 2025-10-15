# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        here rather than reversing, we use stacks. one stack for each LL, so we push them in, so as we pop, we get the digits at the back first, 
        which is what we need. here, we also do not need the dummy node (could have done without it in the reversing approach too tbh) 
        as we create nodes we point them to head, which initially is None, then shift head pointer to the node we just created, at the end of it all, 
        head would point to the beginning of the answer as we want it

        TC: O(M + N)
        SC: O(M + N) because of the stack
        '''


        stack1 = []
        stack2 = []

        carry = 0
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        head = None

        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            total = val1 + val2 + carry
            remainder = total % 10
            carry = total // 10
            node = ListNode(remainder)
            node.next = head
            head = node

        return head
        '''
        Here, we reverse each LL then the question basically becomes Add Two Numbers (LC Question 2), then after the addition, we unlink the dummy 
        and then returned the reverse of the new LL

        note that a solution of going through L1 and turning it to a number, then doing the same for L2, then summing the numbers, and making the digits back to an
        LL to be returned won't work here since the size of eeach LL could be of 100 nodes, it would be greater than what any 32 or 64 bit integer can hold

        TC: O(M + N) where M is the length of L1 and L2 respectively
        SC: O(max(M, N))
        '''
        dummy = ListNode()
        curr = dummy
        curr1, curr2 = self.reverseLL(l1), self.reverseLL(l2)

        carry = 0
        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            total = val1 + val2 + carry
            remainder = total % 10
            curr.next = ListNode(remainder)
            carry = total // 10

            curr = curr.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None

        res = dummy.next
        dummy.next = None

        return self.reverseLL(res)    

    def reverseLL(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


        