class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        slow = fast = head
        # first find if they meet again confirming the presence of a loop, else return 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                break
        else: return 0

        # Here count all the elements after where they meet till when mark becomes slow again, that means you've gone round the loop
        # we don't need to find the beginning of the cycle before we start counting, wherever the fast and slow meet, once we go round again till that point, we have the number of nodes in the cycle
        count = 1
        mark = slow.next
        while mark != slow:
            count += 1
            mark = mark.next
        return count
    
        # another way to do this would have been to use a set. but that would be linear memory