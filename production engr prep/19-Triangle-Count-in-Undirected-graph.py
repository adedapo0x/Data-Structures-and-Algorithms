'''
triangle count in an undirected graph

You are given a list of edges representing an undirected graph.
Each edge is a pair of nodes (u, v), meaning there is a connection between node u and node v.
A triangle (also called a rig) is a set of three distinct nodes A, B, C such that all three edges (A,B), (B,C), and (A,C) exist in the graph.

Write a function that takes the list of edges and returns the total number of triangles in the graph.

notes:
- The graph is undirected, so (A, B) and (B, A) represent the same edge.
- The input may contain duplicate edges.
- The graph may have multiple disconnected components.
- Self-loops should be ignored.

Example:
Input:  [("A","B"), ("B","C"), ("A","C"), ("C","D"), ("D","E"), ("C","E")]
Output: 2

Explanation:
  Triangle 1: A - B - C
  Triangle 2: C - D - E
'''

from collections import defaultdict

def count_rigs(edges_list):
    '''
    The approach here is:
    we are getting a list of edges that can contain reverse edges and duplicate edges or even self loops
    reverse edges: (A, B) and (B, A) represent the same edge in an undirected graph, we only care about it once, so we have to normalize the edges
                    for each edge we see, we bring the minimum amongst them as first element, and max as second. so if we get (A, B) we add (A, B) 
                    and if we then see (B, A) it still results to (A, B) and no duplicates is inserted since a set doesn't allow duplicates
    duplicate edges: seeing (A, B) and (A, B) again has no effect. once it is added into the set once, it cannot be added again
    self loops: we check if u != v, and only add to edges if that is the case, so there are no self loops

    we then create a adjacency list that maps each nodes to a set of its neighbours. we need this because for each edge which contains two nodes already, to find the third node
    that connects them to make a triangle, we need to check what is common across the set of neighbours of both nodes
    we use a set instead of a list because when we want to compare the neighbours, we need to be able to check in O(1) to be more efficient instead of a list O(n) time

    then for each edge in edges, it contains two nodes, we check for the intersection (what both of them are neighbours of) from the adjacency map
    then add to our count.
    we divide the final answer by 3 because a triangle has 3 edges and for each edge, we get the intersection and increment count, so one triangle adds 3 to the count
    e.g for [(A, B), (B, C), (A, C)].
    if we check intersection of node A and B, we get {C} , count += 1
    if we check intersection of node B and C, we get {A} , count += 1
    if we check intersection of node A and C, we get {B} , count += 1

    so we see that for just one triangle, it adds 3 to the count so to get the true amount of triangles present we divide by 3

    TC: O(E * V) 
    to create edges is O(E), to create adjacency list is also O(E), but to compare in worst case is O(E * V)
    since we go through all edges and check its neighbours, in graphs were almost all the nodes are connected, we have compare V nodes for each E
    so TC = O(E + E + (E * V)) so worst case is O(E * V)

    SC: O(V + E) 
    edges is O(E), adjacency matrix is the O(V + E), we store nodes as key and each edge adds to the values of two keys. 
    so in general O(V + E)   
    '''

    # remove reverse edges: if we see (A, B) and (B, A) they represent the same edges
    # and removes duplicates also, seeing (A, B) twice
    edges = set()
    for u, v in edges_list:
        if u != v: # prevent self loop
            edges.add((min(u, v), max(u, v)))

    adjacency_list = defaultdict(set)
    for u, v in edges:
        adjacency_list[u].add(v)
        adjacency_list[v].add(u)

    count = 0
    for u, v in edges:
        count += len(adjacency_list[u] & adjacency_list[v])

    rigs = count // 3
    return rigs
