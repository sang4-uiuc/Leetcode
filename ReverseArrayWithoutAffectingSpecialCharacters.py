def reverseSpecial(s):
  
  l = [i for i in s if i.isalpha()]
  l.reverse()
  
  # print(l)
  for i in range(len(s)):
    if not s[i].isalpha():
      l.insert(i, s[i])
      
      
  return "".join(l)


print(reverseSpecial("Ab,c,de!$"))