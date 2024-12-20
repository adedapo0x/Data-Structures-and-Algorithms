class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        count = 0 # count to check position since the left and right are indices but the LL is 1 indexed
        temp = []
        while curr:
            count += 1
            if count >= left and count <= right:
                temp.append(curr.val)    # add to temp array if within left and right range
            curr = curr.next
        curr = head
        count = 0
        indx = len(temp) - 1
        while curr:
            count += 1
            if count >= left and count <= right:
                curr.val = temp[indx]    # takes input from the reverse of the array and put it as val of LL as we traverse
                indx -= 1                   # from left to right
            if count > right:
                break
            curr = curr.next

        return head