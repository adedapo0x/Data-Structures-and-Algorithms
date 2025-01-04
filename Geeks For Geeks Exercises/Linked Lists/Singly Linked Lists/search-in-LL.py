'''
Given a linked list of n nodes and a key, the task is to check if the key is present in the linked list or not.
'''

class Solution:
    def searchKey(self, n, head, key):
        curr = head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False