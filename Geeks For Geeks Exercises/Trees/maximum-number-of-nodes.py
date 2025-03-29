'''
Given an integer i. Print the maximum number of nodes on level i of a binary tree.

Example 1:
Input: 5
Output: 16

Example 2:
Input: 1
Output: 1

'''

class Solution:
    def countNodes(self, i):
        # Observe the pattern that emerges for each level when nodes are maximum
        return 2 ** (i - 1)