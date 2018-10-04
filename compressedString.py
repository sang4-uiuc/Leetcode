def compressedString(s):
    compressedS = ""
    arr = []
    count = 0
    for i in range(len(s)):
        if i == len(s) - 1 or s[i] != s[i+1]:
            count += 1
            compressedS += s[i]
            compressedS += str(count)
            count = 0
        else:
            count += 1

    if len(s) > len(compressedS):
        
        return compressedS
    else: 
        return s

print(compressedString("aabcccccaaa"))
#a2b1c5a3