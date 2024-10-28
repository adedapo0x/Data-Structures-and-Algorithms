# Write a function sumNumbersRecursive that takes in an array of numbers and returns the sum of all the numbers in the array. 
# All elements will be integers. Solve this recursively.


def sum_numbers_recursive(numbers):
  if len(numbers) == 0:
    return 0

  return numbers[0] + sum_numbers_recursive(numbers[1:])
