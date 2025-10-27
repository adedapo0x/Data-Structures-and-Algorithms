# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Approach here is to use BFS to go level by level and as we go level by level we keep track of the column at which we saw each node.
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
    


    '''
    Approach here is using a DFS. we start from the root and explore downwward, since unlike BFS, DFS doesn't give you that assuredness that the rows are in order from top to 
    bottom, we have to store the row also. so we can rearrange after.
    the hashmap stores colNumber -> [rowNumber, nodeValue]

    the dfs call notes the row and col and value in the hashmap, then recursive call made for it's left and right children. as we go down, the row always
    increases but as when we go left, col - 1, go right, col + 1. we keep track of the minCol and maxCol as we explore the tree, so we don't have to iterate over the hashmap to get that later
    then after we have every node's row, col and val stored in the hashmap,,we then ngo through the cols from minCol to maxCol, sort the values of each col by their row number
    and take the values of the nodes after they are sorted by their rows

    if n is number of nodes, O(N) for dfs call
    if h is height of tree, and w is width of tree, O(w.hlogh) from sorting the rows for each column

    SC: O(N) hashmap
    '''

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        columns = defaultdict(list)
        minCol = maxCol = 0

        def dfs(node, row, col):
            if not node:
                return
            nonlocal minCol, maxCol
            columns[col].append((row, node.val))
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        res = []
        for col in range(minCol, maxCol + 1):
            columns[col].sort(key= lambda x: x[0])
            res.append([nodeValue for row, nodeValue in columns[col]])
        return res
        



# Less optimal, Still same BFS approach, but here we sort the keys rather than maintaining minCol and maxCol from the start
# TC: O(NlogN), SC: O(N)
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        columns = defaultdict(list)
        queue = collections.deque([(root, 0)])

        while queue:
            node, col = queue.popleft()
            columns[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        return [columns[c] for c in sorted(columns)] 