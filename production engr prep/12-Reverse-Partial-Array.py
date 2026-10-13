'''
Question here is to reverse a specific portion of an array
start and end indexes are given to note the portion of the array to be reversed
'''

def reverse_partial_array(arr, start_index, end_index):
    '''
    We use the two pointer approach to reverse the array in place. 
    we start with two pointers, one at the start index and the other at the end index. we swap the elements at these two pointers 
    and then move the pointers towards each other until they meet or cross each other.
    TC: O(N) where N is the difference between the start and end indexes
    SC: O(1)
    '''
    
    if start_index < 0 or start_index > end_index or end_index >= len(arr):
        raise ValueError("Invalid indexes provided")
        
    left_ptr, right_ptr = start_index, end_index
    while left_ptr < right_ptr:
        arr[left_ptr], arr[right_ptr] = arr[right_ptr], arr[left_ptr]
        left_ptr += 1
        right_ptr -= 1
        
    return arr