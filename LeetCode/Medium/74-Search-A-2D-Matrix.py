class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Optimal solution, a binary search on the matrix array itself to find the most suitable array that can contain the target, then after finding 
        # that we perform binary search on that particular inner array to check for the target
        # TC: O(log(M) + log(N)) = O(log(MN)), SC: O(1), where M is the size of the matrix and N the size of the inner array chosen
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid -1 
            else:
                break

        if not l <= r: # i.e if the loop did not end due to the break statement, rather it ended due to l now being greater than r, ie the 
            return False # else statement didn't run so we know the matrix cannot contain our target and return False

        l,r = 0, len(matrix[mid]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[mid][m] == target:
                return True
            elif matrix[mid][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False

        ## This is one implementation of the solution for this problem, came up with this myself. Perform binary search on the outer array and binary search on 
        # the elements of the matrix which are arrays too
        # Note, not very optimal as we are performing a complete binary search on every matrix[mid] that could potentially contain target, rather than finding the one
        # most likely to contain the target and then performing the binary search on as done above 
        # So basically perforing binary search while performing a outer binary search 
        # TC: O(log(N)xlog(M))
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
