# Write a function, five_sort, that takes in a list of numbers as an argument. 
# The function should rearrange elements of the list such that all 5s appear at the end. 
# Your function should perform this operation in-place by mutating the original list. 
# The function should return the list.

# Elements that are not 5 can appear in any order in the output, 
# as long as all 5s are at the end of the list.


def five_sort(nums):
  l, r = 0, len(nums) - 1

  while l < r:
    if nums[r] == 5:
      r -= 1
      continue

    if nums[l] != 5:
      l += 1
      continue
    
    nums[l], nums[r] = nums[r], nums[l]
    r -= 1
    l += 1

  return nums    