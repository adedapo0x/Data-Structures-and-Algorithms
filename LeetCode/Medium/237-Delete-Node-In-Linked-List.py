class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # More of a change of identity than deletion of the actual node
        # Since node values are unique, just change the node to be deleted to the one after it in value and where it's next pointer points to
        # TC: O(1), SC: O(N)

        node.val = node.next.val
        node.next = node.next.next

        # same logic, my first implementation, more verbose code using a loop and all, no need for a loop
        # curr = node
        # while curr:
        #     curr.val = curr.next.val
        #     if curr.next.next:
        #         curr = curr.next
        #     else:
        #         break
        # curr.next = None