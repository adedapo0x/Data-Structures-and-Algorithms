class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## This is one implementation of the optimal solution for this problem, came up with this myself. Perform binary search on the outer array and binary search on 
        # the elements of the matrix which are arrays too
        # So basically perforing binary search while performing a outer binary search 
        # TC: O(log(NM))
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            lmin, rmin = 0, len(matrix[mid]) - 1
            while lmin <= rmin:
                midMin = (lmin + rmin) // 2
                if matrix[mid][midMin] == target:
                    return True
                elif matrix[mid][midMin] > target:
                    rmin = midMin - 1
                else:
                    lmin = midMin + 1
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] < target:
                l = mid + 1 

        return False
    
        # Better solution would be to use to traverse through the array, since they are sorted find the one whose range contains the target we are looking for,
        # then perform binary search on that particular array to find the target
        # TC: O(N.logM), N is the outer array, N the inner

    
        # Bruteforce solution would be to use the two loops, traverse through the 2D matrix, and check if the target exists in any of the
        # element arrays, if so return True. TC: O(N.M), SC: O(1), where N is the size of the outer array, and M the size of the largest inner array
