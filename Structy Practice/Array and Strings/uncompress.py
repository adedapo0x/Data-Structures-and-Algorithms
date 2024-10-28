# Write a function, uncompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:

# <number><char>
# for example, '2c' or '3a'.

# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.

def uncompress(s):
  res = []
  l, r = 0, 0

  while r < len(s):
    if s[r].isdigit():
      r += 1
    else:
      length = int(s[l:r])
      res.append(s[r] * length)
      r += 1
      l = r
  return "".join(res)
       
      
      