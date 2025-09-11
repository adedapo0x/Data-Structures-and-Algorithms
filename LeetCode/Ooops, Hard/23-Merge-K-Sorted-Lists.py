class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        Here the approach is to use the logic of the question merge two sorted LL (LC 21) to sort multiple LLs
        so we basically iterate through the list of LLs, taking two at a time and merging them, we start from index 1, so we take LL at 0 and 1, sort,
        place the sorted in index 1, then loop increments i, then we merge the merged result in 1 with the new LL in index 2, rinse repeat
        we find out that at the end, the final merged sorted LL that contains all the LL is in the last index of the lists array
        and we can then return this.

        TC: O(N * K) since worst case scenario we have to go through each LL to merge and this occurs k times, since we are traversing through the lists array 
        of size k
        SC: O(1), no extra space was used
        '''
        if not lists:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoList(lists[i - 1], lists[i])

        return lists[-1]
            
    def mergeTwoList(self, list1, list2):
        dummy = ListNode()
        temp = dummy
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                temp.next = curr1
                curr1 = curr1.next
            else:
                temp.next = curr2
                curr2 = curr2.next
            temp = temp.next
        if curr1:
            temp.next = curr1
        if curr2:
            temp.next = curr2
        return dummy.next



        """
        Bruteforce approach is to go through each LL one after the other while storing their values in an array, then sort those values
        then go through the sorted array, creating nodes of each val and linking them to each other

        TC: O(NlogN) where N is the total number of nodes in the linked lists in the lists array
        technically we have O(N) getting values, O(NlogN) sorting, O(N) creating linked nodes again. so yeah, O(NlogN) is the dominant term
        SC: O(N) used to store the node values 
        """

        nodes = []
        for li in lists:
            while li:
                nodes.append(li.val)
                li = li.next

        nodes.sort()

        dummy = ListNode()
        curr = dummy

        for val in nodes:
            node = ListNode(val)
            curr.next = node
            curr = curr.next

        return dummy.next

