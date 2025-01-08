'''
Given two sorted arrays a[] and b[], where each array may contain duplicate elements , 
the task is to return the elements in the union of the two arrays in sorted order.
Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.
'''

class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # More optimal approach to solving the problem, still uses two pointers but without the hashmap
        # TC: O(n + m) where n and m are the length of the input array a and b respectively
        # SC: O(n + m) in worst case scenario, where there are no duplicates

        ptrA = ptrB = 0
        res = []
        lenA, lenB = len(a), len(b)
        while ptrA < lenA and ptrB < lenB:
            # This is used to handle duplicates in array a, loops until the next element isn't the same as current
            while ptrA + 1 < lenA and a[ptrA + 1] == a[ptrA]:
                ptrA += 1
            # for array b
            while ptrB + 1 < lenB and b[ptrB + 1] == b[ptrB]:
                ptrB += 1
                
            if a[ptrA] < b[ptrB]:
                res.append(a[ptrA])
                ptrA += 1
            elif b[ptrB] < a[ptrA]:
                res.append(b[ptrB])
                ptrB += 1
            else:
                res.append(a[ptrA])
                ptrA += 1
                ptrB += 1
                
        # if one loop still remain, that is one of them is larger
        while ptrA < lenA:
            while ptrA + 1 < lenA and a[ptrA + 1] == a[ptrA]:
                ptrA += 1
            
            res.append(a[ptrA])
            ptrA +=1 
            
        while ptrB < lenB:
            while ptrB + 1 < lenB and b[ptrB + 1] == b[ptrB]:
                ptrB += 1
            
            res.append(b[ptrB])
            ptrB += 1
            
        return res






        # Brute force kind of solution. This uses a hash map to make sure there are no duplicates. Two pointers approach is used to traverse through both the input array
        ptrA = ptrB = 0
        hashMap = {}
        res = []
        while ptrA < len(a) and ptrB < len(b):
            if a[ptrA] == b[ptrB] and a[ptrA] not in hashMap:
                # print(a[ptrA], sep=" ")
                res.append(a[ptrA])
                hashMap[a[ptrA]] = 0
                ptrA += 1
                ptrB += 1
            elif a[ptrA] == b[ptrB]:
                ptrA += 1
                ptrB += 1
            elif a[ptrA] < b[ptrB] and a[ptrA] not in hashMap:
                # print(a[ptrA], sep=" ")
                res.append(a[ptrA])
                hashMap[a[ptrA]] = 0
                ptrA += 1
            elif a[ptrA] < b[ptrB]:
                ptrA += 1
            elif b[ptrB] < a[ptrA] and b[ptrB] not in hashMap:
                # print(b[ptrB], sep=" ")
                res.append(b[ptrB])
                hashMap[b[ptrB]] = 0
                ptrB += 1
            elif b[ptrB] < a[ptrA]:
                ptrB += 1
            
                
        while ptrA < len(a):
            if a[ptrA] not in hashMap:
                # print(a[ptrA], sep=" ")
                res.append(a[ptrA])
                hashMap[a[ptrA]] = 0
            ptrA += 1
            
        while ptrB < len(b):
            if b[ptrB] not in hashMap:
                # print(b[ptrB], sep=" ")
                res.append(b[ptrB])
                hashMap[b[ptrB]] = 0
            ptrB += 1
            
        return res