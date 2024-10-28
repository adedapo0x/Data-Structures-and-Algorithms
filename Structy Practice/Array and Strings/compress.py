# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

# You can assume that the input only contains alphabetic characters.

def compress(s):
  l, r = 0, 0
  count = 0
  res = []

  while r < len(s):
    if s[r] == s[l]:
      count += 1
      r += 1
    else:
      res.append((str(count) + s[l]) if count > 1 else s[l])
      count = 0
      l = r
  res.append((str(count) + s[l]) if count > 1 else s[l])
  return "".join(res)
      
      
    
    
    