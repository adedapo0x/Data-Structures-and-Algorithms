# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # clean recursive DFS solution, uses like preorder traversal. 
        # TC: O(p + q)
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        return False # handles condition when one is null, the other is a node, and also when both are nodes but their values are not equal


        # using BFS (level order traversal)
        # set one queue for each tree, be popping and adding as usual while comparing, note: None also gets appended to the queue unlike in
        # traditional BFS
        if not p and not q:
            return True

        pQueue = collections.deque([p])
        qQueue = collections.deque([q])
        while pQueue and qQueue:
            for i in range(len(pQueue)):
                pNode = pQueue.popleft()
                qNode = qQueue.popleft()

                if qNode is None and pNode is None:
                    continue
                if pNode is None or qNode is None or pNode.val != qNode.val:
                    return False
                
                pQueue.append(pNode.left)
                pQueue.append(pNode.right)
                qQueue.append(qNode.left)
                qQueue.append(qNode.right)
        return True
    

        # similar thing for using iterative DFS. But this time, we do it with just a single stack, that initially contains (p,q)
        # then we pop, check if those conditions, and add their children in the same format, appending None also
        #   Check neetcode implementation to understand better
        

        # came up with this solution myself, lmao. not straightforward at all, an AC tho, so a W for me
        # did a postorder traversal on this one 
        if not p and not q:
            return True
        if (p and not q) or (q and not p): return False
        left = self.isSameTree(p.left, q.left)
        if not left: return False
        right = self.isSameTree(p.right, q.right)
        if not right: return False
        return p.val == q.val


        