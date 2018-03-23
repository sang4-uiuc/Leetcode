# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


def reverseSpecial(s):
  
  l = [i for i in s if i.isalpha()]
  l.reverse()
  
  # print(l)
  for i in range(len(s)):
    if not s[i].isalpha():
      l.insert(i, s[i])
      
      
  return "".join(l)


print(reverseSpecial("Ab,c,de!$"))