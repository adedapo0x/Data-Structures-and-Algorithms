class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        One way to go about solving this would be to use a list. traverse the LL and put the nodes in a list. Then we can use two pointers,
        one in the beginning, one in the end to check if the nodes in the array are palindrome
        # TC: O(N), SC: O(N)

        More optimal way would be to use two pointers, a fast and slow pointer, to get the middle of the linked list,
        reverse the LL from the middle down to the end then we can now compare the values, traversing from the head and the new head of the reversed LL to check if they are equal
        we keep this up till the reversed LL is finished
        TC: O(N), SC: O(1)
        '''




        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True