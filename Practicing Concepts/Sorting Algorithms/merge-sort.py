# This is a recursive sorting algorithm that involves dividing and merging

# The mergeSort function takes in three parameters; the unsorted array, the leftmost index of the array (typically 0), the rightmost index of the array (len(arr) - 1)
# Initially, the array is hypothetically divided into two parts (hypothetical in the sense that we do this in terms of the array's index and no division that requires creating of another array happens)
# The first part, which is the left part is further splitted again and again till they can be no more splits, then the individual elements are sorted using a merge() function then are merged back
# Since it is a recursive function, the merging only starts after the division is complete and each element is in its own hypothetical array then it returns and returns while being merged. 
# The same happens for the second/right part


# As for the merge function, it takes in 4 parameters; the array, left, mid and right indexes
# Two pointers, l and r are created, whereby the left pointer is initially assigned to the left index and is used to traverse up to middle index
# The right pointer is initially instantiated as the next index after mid(mid + 1) and traverses till it gets to the end of the array(right)
# A temporary array to store the sorted form of the array is also created 

# to traverse, it checks which is smaller, element at l index or the one at r index, whichever is, it updates the temp array by appending it to it and incrementing the index with the smaller value
# this goes on until one side is exhausted, then the rest of the other side is simply added to the end of the temp array, since each side would be sorted before the merge is called

# the input array is then updated by traversing through the indexes (left to right) and updates are made

