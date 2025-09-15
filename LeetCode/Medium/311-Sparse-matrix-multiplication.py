class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        '''
        Optimal way of solving this problem
        the meaning of sparse matrix is that many of the elements in the matrix is 0. so it is redundant to try to calculate if we still end up with 0 at the end.
        we can prefill the res array with 0 and only compute the part with actual elements to reduce unnecessary computations.

        the idea here is that we create a hashmap for each matrix, both would be a hashmap of a hashmap
        of the form { i1: {k1: val, k2: val}, i2: {v1: val} }
        so here i1 or i2 is the row of the input matrix and serves as key in the hashmap, k is the col where non-zero value exists for that row, and val is the actual element that was non zero in the matrix
        so this way we do that for both matrices to get rid of the 0s and also be able to compute fast using hashmap O(1) lookup advantage

        so in order to multiply, we still need to use the formular given in the bruteforce, only difference is no computing those with 0
        the formular is res[i][j] += (mat1[i][k] * mat2[k][j])

        so we go through each index in our hashMap1 (which contains our rows in mat1 as keys), then we go through its cols for that row that has non zero values
        as those are only what is stored in the hashmap, if for that particular column k in mat1 there is no corresponding row entry in hashMap2 for mat2, means there are no
        non-zero values and the formular mat2[k][j] would fail, so we continue,
        but if the k exists in hashMap2, ie there is a row k that has non zero values, and we then use it for our res[i][j] calculation
        we get j (col in mat2) from it and the actual value stored 
        '''
        
        m, n, p = len(mat1), len(mat1[0]), len(mat2[0])

        hashMap1 = {}
        hashMap2 = {}

        for i in range(m):
            for k in range(n):
                if mat1[i][k] != 0:
                    if i not in hashMap1:
                        hashMap1[i] = {}
                    hashMap1[i][k] = mat1[i][k]

        for k in range(n):
            for j in range(p):
                if mat2[k][j] != 0:
                    if k not in hashMap2:
                        hashMap2[k] = {}
                    hashMap2[k][j] = mat2[k][j]

        res = [[0] * p for i in range(m)]

        for i in hashMap1:
            for k, val1 in hashMap1[i].items():
                if k not in hashMap2: # following the formular we need to check unless that hashMap2[k] might generate an error
                    continue
                
                for j, val2 in hashMap2[k].items():
                    res[i][j] += val1 * val2
        
        return res
        

                
        '''
        Here is the bruteforce approach, for 2 matrices m x n and n x p to multiply, the col in one equal to row in the other ie n == n
        the resultant matrix will be of the size m x p.

        so here to get the formular to work with, we basically write out how we get each individual index in the resultant array (which is the sum 
        of the multiplications of a row to a col basically) normal matrix multiplication

        we notice a pattern that for
        res[i][j] += mat1[i][k] * mat2[k][j] ie for a position [i][j] in the resultant array, the i and j remain constant in calculation only the one labelled k goes from 0 to n - 1

        so we basically use this formualar generated to solve this problem, got the i and j loop from res since we can already tell its size , easier to think of that way
        
        so TC: O(i*j*k) which is obviously not optimal
        '''
    

        # res = [[0] * len(mat2[0])  for i in range(len(mat1))]

        # for i in range(len(res)):
        #     for j in range(len(res[i])):
        #         for k in range(len(mat2)):
        #             res[i][j] += (mat1[i][k] * mat2[k][j])

        # return res
