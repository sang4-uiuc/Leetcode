def decrypt(word):
  secondStep = 1
  decryp = ""
  for i in range(len(word)):
    newLetter = ord(word[i])
    newLetter = newLetter - secondStep
    while(newLetter < ord('a')):
      newLetter += 26
    decryp += chr(newLetter)
    secondStep += newLetter
  
  return decryp

def decrypt2(word):
  secondStep = []
  secondStep.append(1)
  decryp = ""
  for i in range(len(word)):
    newLetter = ord(word[i])
    newLetter = newLetter - secondStep[i]
    while(newLetter < ord('a')):
      newLetter += 26
    decryp += chr(newLetter)
    secondStep.append(newLetter + secondStep[i])
  
  return decryp


print(decrypt2("dnotq"))