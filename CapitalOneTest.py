# Given a string, return the first NON-repeating character that occurs in the string.
# EX: "adzbdcab" returns 'z'.  


def noRepeat(s):
    dic = {}
    for i, c in enumerate(s):
        if c in dic:
            dic[c] = len(s)
        else:
            dic[c] = i
    print(dic)
    return min(dic, key =dic.get)

def getFirst(l):
    return min(l.values())

print(noRepeat("adzbdcab"))