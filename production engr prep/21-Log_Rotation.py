'''
You are building a simplified log rotation system. A server maintains a current log file app.log and a series of older log files app.log.1, app.log.2, ..., where higher numbers are older.

When rotation is triggered:

Each file shifts one position: app.log becomes app.log.1, app.log.1 becomes app.log.2, and so on.
A new, empty app.log is created.
Any old files beyond the keep limit K are deleted.
Input
Line 1: An integer K, the maximum number of old files to keep.
Line 2: The contents of each file, space-separated, in order from app.log (leftmost) to the oldest file (rightmost). Each entry is a non-empty string representing that file’s contents.
Output

Print the contents of each file after rotation in the same space-separated format. The new empty app.log is represented as -.

Constraints
1 ≤ K ≤ 100
There will be at least 1 file in the input.
Examples

Example 1:

Input:
2
v3 v2 v1

Output:
- v3 v2

Example 2:

Input:
1
a b c

Output:
- a
'''
import sys
def rotate_log():
    k = int(next(sys.stdin).strip())
    contents = next(sys.stdin).strip().split()
    
    contents = ["-"] + contents
    
    result = contents[:k + 1] # basically just gets k + 1 elements
    
    print(" ".joined(result))
    
    