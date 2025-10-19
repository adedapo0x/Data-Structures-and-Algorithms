"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        Here we improve the SC to be O(1), we get rid of the queue
        the way we do this is that when we are at a level N, we want to connect the nodes at level N + 1 together with their .next

        the way to do this is we use three variables, curr, dummy and tail
        curr is the node we are currently on, dummy is the dummy node we put in front of the next level we would be going to, we said we are at level N
        so we put dummy at beginning of level N + 1, then tail is a pointer that is used to connect the nodes at N + 1, it starts at dummy, then when we see the next available node at that
        level, we put tail.next to that and move tail to there

        so basically after we are done traversing a level N, the entire nodes in level N + 1, would have already been connected and to go to level N + 1
        we just need to go to dummy.next as that would point to the first node in that level, and we can do rinse and repeat for each level

        '''
        if not root:
            return root

        curr = root
        while curr:
            dummy = Node()
            tail = dummy
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            curr = dummy.next
        return root



        '''
        Here we use a queue to do normal BFS, it doesn't matter if some nodes are absent for a particular level. the BFS would keep track of all the available nodes for a particular
        level and these are the ones we have interest in connecting their next together. so we keep on connecting their .next together as long as the queue is of size 2 and above, 
        cos if the queue gets reduced to size 1, we then pop, there would be nothing in queue[0] for us to connect to

        TC: O(N), SC: O(N)
        '''
        if not root:
            return root
        queue = collections.deque([root])

        while queue:
            size = len(queue)
            while size > 0:
                node = queue.popleft()
                if size > 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
        return root

        