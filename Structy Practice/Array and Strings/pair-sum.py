# Write a function, pair_sum, that takes in a list and a target sum as arguments. 
# The function should return a tuple containing a pair of indices whose elements sum to the given target. 
# The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair that sums to the target.


def pair_sum(numbers, target_sum):
  number_hash = {}

  for i in range(len(numbers)):
    diff = target_sum - numbers[i]

    if diff in number_hash:
      return (number_hash[diff], i)
      
    number_hash[numbers[i]] = i 
  