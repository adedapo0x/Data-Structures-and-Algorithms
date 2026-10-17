'''
Your team merged n check-ins into a branch in chronological order. Quality is monotone: once a check-in is bad (B), 
every later one is bad too, because the bug is never fixed. Earlier ones are good (G).
Find the first bad check-in, which is exactly what git bisect does. 
In real life each probe is an expensive build and test, so the number of probes should be O(log n).

Approach: we could solve this in linear time by just scanning through the string and getting the index of the first B in O(N) time complexity
a better approach is to use binary search, we are guaranteed that all the G are at one side and all the B are at one side, we just need to find where the B
starts from, with a more optimal TC of O(logN)g
'''

def get_first_bad_entry(check_ins):
    low, high = 0, len(check_ins) - 1
    
    while low < high:
        mid = (low + high) // 2
        if check_ins[mid] == "G":
            low = mid + 1
        else:
            high = mid
    return low + 1


def main():
    check_ins = input().strip()
    print(get_first_bad_entry(check_ins))


if __name__ == "__main__":
    main()