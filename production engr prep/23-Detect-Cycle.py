from collections import defaultdict
def has_cycle(n, edges):
    '''
    use colors to denote state, if white, we haven;t seen before in this run, if gray we have seen before, this is a cycle return True
    if black, then we have ran by it before and it didn't produce a cycle so do not use it
    '''
    adjacency_list = defaultdict(list)
    for u, v in edges:
        adjacency_list[u].append(v)
        
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in adjacency_list}
    
    def dfs(node):
        color[node] = GRAY  
        
        for neighbour in adjacency_list[node]:
            if color[neighbour] == GRAY:
                return True
            if color[neighbour] == WHITE:
                if dfs(neighbour):
                    return True

        color[node] = BLACK
        return False
        
    for node in adjacency_list:
        if color[node] == WHITE:
            if dfs(node):
                return True
            
    return False