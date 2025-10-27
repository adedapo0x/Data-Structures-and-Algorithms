# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Approach here is to use DFS to go level by level and as we go level by level we keep track of the column at which we saw each node.
    we use a hashmap to store the nodes on the same col, and we have them in the correct order since we are going top to bottom through my BFS. 
    hashmap stores colNum -> [nodes in that col], and since the way we return the nodes in the col is expected to follow each other, we maintain a minCol
    and a maxCol variable as we know that will be the range of columns we have as keys in the hashmap

    for the column numbering, we take the root node as col 0, then what is at the left as col - 1, what is at the right as col + 1, we do that for every node
    so the columns we get ends up ranging from negative to positive

    TC: O(N), SC: O(N)
    
    '''
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        queue = collections.deque([(root, 0)])
        columns = defaultdict(list)
        minCol, maxCol = 0, 0

        while queue:
            node, col = queue.popleft()
            minCol, maxCol = min(minCol, col), max(maxCol, col)
            columns[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
            
        return [columns[col] for col in range(minCol, maxCol + 1)]