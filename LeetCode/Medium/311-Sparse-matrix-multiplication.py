class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        '''
        Optimal way of solving this problem
        the meaning of sparse matrix is that 
        '''
        
        m, n, p = len(mat1), len(mat1[0]), len(mat2[0])

        hashMap1 = {}
        hashMap2 = {}

        for i in range(m):
            hashMap1[i] = {}
            for k in range(n):
                if mat1[i][k] != 0:
                    hashMap1[i][k] = mat1[i][k]

        for k in range(n):
            hashMap2[k] = {}
            for j in range(p):
                if mat2[k][j] != 0:
                    hashMap2[k][j] = mat2[k][j]

        res = [[0] * p for i in range(m)]

        for i in range(m):
            for k, val1 in hashMap1[i].items():
                if k not in hashMap2:
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
