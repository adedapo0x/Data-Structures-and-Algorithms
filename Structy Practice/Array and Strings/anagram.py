# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams.
#  Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
  hash1, hash2 = {}, {}

  for c1 in s1:
    hash1[c1] = hash1.get(c1, 0) + 1

  for c2 in s2:
    hash2[c2] = hash2.get(c2, 0) + 1

  return hash1 == hash2