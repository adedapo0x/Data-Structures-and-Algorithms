# Write a function, most_frequent_char, that takes in a string as an argument. 
# The function should return the most frequent character of the string. 
# If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.

def most_frequent_char(s):
  count = {}

  for char in s:
    count[char] = count.get(char, 0) + 1

  max, maxChar = 0, ''
  
  for key, val in count.items():
    if val > max:
      max = val
      maxChar = key

  return maxChar
      


    